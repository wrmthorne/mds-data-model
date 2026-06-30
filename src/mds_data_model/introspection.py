from __future__ import annotations

from functools import cache
from typing import get_args

from pydantic import BaseModel

from .models import all_models
from .models.common import ControlledVocab
from .models.date import Date
from .models.object import Object


def _annotation_contains(annotation: object, target: type) -> bool:
    """Return True if ``target`` appears anywhere in ``annotation``.

    Walks the annotation recursively, so ``target`` is found whether it stands alone (``x: Date``), sits in a union
    (``x: Date | str | None``), or is nested inside a container or annotated type (``x: list[Date | str]``,
    ``Annotated[Date, ...]``).
    """
    if annotation is target:
        return True
    return any(_annotation_contains(arg, target) for arg in get_args(annotation))


@cache
def fields_of_type(model: type[BaseModel], target: type) -> tuple[str, ...]:
    """Names of ``model`` fields whose declared type includes ``target``.

    Matches ``target`` whether it stands alone, appears in a union, or is nested in a container. The result is cached
    per ``(model, target)`` pair: it is computed once on first call and returned in O(1) thereafter, so it is safe to
    call repeatedly. The returned tuple is immutable to keep the cached value from being mutated by callers.
    """
    return tuple(name for name, field in model.model_fields.items() if _annotation_contains(field.annotation, target))


def date_fields(model: type[BaseModel] = Object) -> tuple[str, ...]:
    """Names of fields that can hold a :class:`Date` (alone or within a union)."""
    return fields_of_type(model, Date)


@cache
def fields_with_metadata(model: type[BaseModel], target: type) -> tuple[str, ...]:
    """Names of ``model`` fields annotated with the ``target`` marker.

    Looks at each field's ``Annotated`` metadata (where Pydantic keeps markers it doesn't otherwise interpret),
    matching whether the marker is supplied as the class itself (``Annotated[str, ControlledVocab]``) or as an
    instance. Cached per ``(model, target)`` pair and returned as an immutable tuple.
    """
    return tuple(
        name
        for name, field in model.model_fields.items()
        if any(meta is target or isinstance(meta, target) for meta in field.metadata)
    )


def vocab_fields(model: type[BaseModel] = Object) -> tuple[str, ...]:
    """Names of fields backed by a controlled vocabulary.

    Finds the :class:`ControlledVocab` marker whether it sits at the top of the annotation (where Pydantic lifts it
    into ``field.metadata``) or nested inside a container such as ``OneOrMany[ControlledTerm]`` (where it stays within
    the annotation). Returned in declaration order as an immutable tuple.
    """
    marked = set(fields_with_metadata(model, ControlledVocab)) | set(fields_of_type(model, ControlledVocab))
    return tuple(name for name in model.model_fields if name in marked)


def all_vocab_fields() -> dict[type[BaseModel], tuple[str, ...]]:
    """Controlled-vocabulary fields for every model, keyed by model class.

    Covers the whole package in one call instead of invoking :func:`vocab_fields` per model. Models with no vocabulary
    fields are omitted. Flatten to a single set of names with ``{n for names in all_vocab_fields().values() for n in
    names}`` if the owning model does not matter.
    """
    return {model: fields for model in all_models() if (fields := vocab_fields(model))}
