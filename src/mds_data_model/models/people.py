from __future__ import annotations

from pydantic import Field

from .common import ControlledVocabField, MDSModel


class People(MDSModel):
    value: str | None = None

    peoples_culture: ControlledVocabField = Field(None,
        description="An identifiable type of civilisation.",
    )
    peoples_association: ControlledVocabField = Field(None,
        description="The way in which a People are associated with a particular object.",
    )
    peoples_group: ControlledVocabField = Field(None,
        description="An identifiable community or division of a nation of People.",
    )
    peoples_linguistic_group: ControlledVocabField = Field(None,
        description="A broad grouping of People identifiable by common linguistic roots.",
    )