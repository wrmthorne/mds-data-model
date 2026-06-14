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


ControlledVocabField = Annotated[list[str] | str | None, ControlledVocab]
