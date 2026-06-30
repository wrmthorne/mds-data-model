from typing import Annotated

from pydantic import BaseModel, ConfigDict


class MDSModel(BaseModel):
    """Base for all MDS models. External data namespaces every property with a prefix."""

    model_config = ConfigDict(
        alias_generator=lambda name: f"spectrum/{name}",
        populate_by_name=True,
    )


class ControlledVocab:
    """Fields that Spectrum indicates should 'Maintain a standard list of terms'.

    Fields with this annotation should be converted to an Enum or Literal as the vocabulary is defined
    """


type OneOrMany[T] = list[T] | T | None
"""A field accepting one or many values of ``T``, or nothing.

For entities that may also be given as a string reference, include ``str`` in ``T``
(e.g. ``OneOrMany[Title | str]``).
"""


ControlledTerm = Annotated[str, ControlledVocab]
"""A single controlled-vocabulary term: a ``str`` carrying the :class:`ControlledVocab` marker.

Wrap in :data:`OneOrMany` for fields that accept one or many terms (``OneOrMany[ControlledTerm]``),
or union with ``None`` for a single optional term (``ControlledTerm | None``).
"""
