from __future__ import annotations

from pydantic import Field

from .common import ControlledVocabField, MDSModel
from .date import Date, DateStringISO
from .location import Location
from .organisation import Organisation
from .person import Person
from .place import Place


class Reference(MDSModel):
    value: str | None = None

    catalogue_number: list[str] | str | None = Field(None,
        description="The number assigned to an object in an exhibition catalogue.",
    )
    document_location: list[Location | str] | Location | str | None = Field(None, # FIXME: controlled
        description="Where a referenced document is stored in an organisation’s documentation system.",
    )
    reference_author_editor: list[Organisation | Person | str] | Organisation | Person | str | None = Field(None,
        description="The Person or Organisation responsible for the intellectual content of a referenced work.",
    )
    reference_association: ControlledVocabField = Field(None,
        description="A single term describing the nature of the relationship between the Reference and an object.",
    )
    reference_details: list[str] | str | None = Field(None,
        description="Details, pages, and illustrations of a bibliographic reference.",
    )
    reference_note: list[str] | str | None = Field(None,
        description="Details of the specific nature of the relevance of the Reference to the object, including an "
            "abstract if required.",
    )
    reference_number: list[str] | str | None = Field(None,
        description="A number or identifier unique to a Reference.",
    )
    reference_publication_date: Date | DateStringISO | None = Field(None,
        description="The Date when a referenced work was published.",
    )
    reference_publication_place: list[Place | str] | Place | str | None = Field(None,
        description="The Place where a referenced work was published.",
    )
    reference_publisher: list[Organisation | Person | str] | Organisation | Person | str | None = Field(None,
        description="The Organisation or Person responsible for the publication of a referenced work.",
    )
    reference_title: list[str] | str | None = Field(None,
        description="The title of a referenced work.",
    )
    reference_type: ControlledVocabField = Field(None,
        description="A term describing the nature of the Reference.",
    )
