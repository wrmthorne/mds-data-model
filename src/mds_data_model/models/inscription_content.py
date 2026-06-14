from __future__ import annotations

from pydantic import Field

from .common import ControlledVocabField, MDSModel
from .date import Date, DateStringISO
from .organisation import Organisation
from .people import People
from .person import Person


class InscriptionContent(MDSModel):
    value: str | None = None

    inscriber: list[Organisation | People | Person | str] | Organisation | People | Person | str | None = Field(None,
        description="The People, Person or Organisation responsible for inscribing an object.",
    )
    inscription_date: Date | DateStringISO | None = Field(None,
        description="The date on which an inscription was made.",
    )
    inscription_description: list[str] | str | None = Field(None,
        description="A description of non-textual marks inscribed on an object.",
    )
    inscription_interpretation: list[str] | str | None = Field(None,
        description="The interpretation of an inscription or mark on an object.",
    )
    inscription_language: ControlledVocabField = Field(None,
        description="The language used in a textual inscription on an object.",
    )
    inscription_method: ControlledVocabField = Field(None,
        description="The method used to inscribe a mark or text on an object.",
    )
    inscription_position: ControlledVocabField = Field(None,
        description="A term describing the position of an inscription on an object.",
    )
    inscription_script: ControlledVocabField = Field(None,
        description="The script used in a textual inscription on an object.",
    )
    inscription_translation: list[str] | str | None = Field(None,
        description="A translation into the organisation's first language of a textual inscription on an object.",
    )
    inscription_transliteration: list[str] | str | None = Field(None,
        description="The transliteration of a textual inscription on an object.",
    )
    inscription_type: ControlledVocabField = Field(None,
        description="The form or function of the inscription.",
    )
