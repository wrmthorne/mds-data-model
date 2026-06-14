from __future__ import annotations

from functools import lru_cache
from typing import get_args

from pydantic import BaseModel

from .models.date import Date
from .models.object import Object


def _annotation_contains(annotation: object, target: type) -> bool:
    """Return True if ``target`` appears anywhere in ``annotation``.

    Walks the annotation recursively, so ``target`` is found whether it stands
    alone (``x: Date``), sits in a union (``x: Date | str | None``), or is nested
    inside a container or annotated type (``x: list[Date | str]``,
    ``Annotated[Date, ...]``).
    """
    if annotation is target:
        return True
    return any(_annotation_contains(arg, target) for arg in get_args(annotation))


@lru_cache(maxsize=None)
def fields_of_type(model: type[BaseModel], target: type) -> tuple[str, ...]:
    """Names of ``model`` fields whose declared type includes ``target``.

    Matches ``target`` whether it stands alone, appears in a union, or is nested
    in a container. The result is cached per ``(model, target)`` pair: it is
    computed once on first call and returned in O(1) thereafter, so it is safe to
    call repeatedly. The returned tuple is immutable to keep the cached value
    from being mutated by callers.
    """
    return tuple(
        name
        for name, field in model.model_fields.items()
        if _annotation_contains(field.annotation, target)
    )


def date_fields(model: type[BaseModel] = Object) -> tuple[str, ...]:
    """Names of fields that can hold a :class:`Date` (alone or within a union)."""
    return fields_of_type(model, Date)