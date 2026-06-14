from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from .common import MDSModel

if TYPE_CHECKING:
    from .common import ControlledVocab, ControlledVocabField
    from .date import Date, DateStringISO
    from .organisation import Organisation
    from .people import People
    from .person import Person


class Place(MDSModel):
    value: str | None = None

    place_reference_number: list[PlaceReferenceNumber | str] | PlaceReferenceNumber | str | None = Field(None,
        description="A code describing a Place associated with an object, excavation or specimen.",
    )
    place_name: list[PlaceName | str] | PlaceName | str | None = Field(None,
        description="The name or title by which the Place is normally known.",
    )
    place_association: ControlledVocabField = Field(None,
        description="The way in which a Place is associated with the object.",
    )
    place_context: list[PlaceContext | str] | PlaceContext | str | None = Field(None,
        description="A number, code or term identifying physical evidence of an archaeological event, such as a wall, "
            "pit or ditch.",
    )
    place_coordinates: list[PlaceCoordinates | str] | PlaceCoordinates | str | None = Field(None,
        description="The precise location of a place expressed according to a chosen system.",
    )
    place_environmental_details: list[str] | str | None = Field(None,
        description="Environmental information relevant to an object, such as details about preservation conditions "
            "of the surrounding matrix.",
    )
    place_feature: list[PlaceFeature | str] | PlaceFeature | str | None = Field(None,
        description="The name by which a feature associated with an object is normally known.",
    )
    place_note: list[str] | str | None = Field(None,
        description="Additional information about Place which has not been recorded elsewhere using controlled "
            "terminology.",
    )
    place_owner: list[Organisation | People | Person | str] | Organisation | People | Person | str | None = Field(None,
        description="The owner of a Place associated with an object.",
    )
    place_position: list[str] | str | None = Field(None,
        description="A precise position in a Place, usually to record the finding of an object in field collection.",
    )
    place_status: ControlledVocabField = Field(None,
        description="A formal administrative or scientific status assigned to a Place.",
    )
    place_type_system: list[str] | str | None = Field(None,
        description="The classification system from which the Place feature type is taken.",
    )


class PlaceReferenceNumber(MDSModel):
    value: str | None = None

    place_reference_number_type: ControlledVocabField = Field(None,
        description="The category of Place reference number recorded.",
    )


class PlaceName(MDSModel):
    value: str | None = None

    place_name_type: ControlledVocabField = Field(None,
        description="The nature or category of Place recorded.",
    )


class PlaceContext(MDSModel):
    value: str | None = None

    place_context_date: Date | DateStringISO | None = Field(None,
        description="The date of a context.",
    )
    place_context_level: list[str] | str | None = Field(None,
        description="A level within a context.",
    )


class PlaceCoordinates(MDSModel):
    value: str | None = None

    place_coordinates_qualifier: list[str] | str | None = Field(None,
        description="The measurement of accuracy of a given for Place coordinates.",
    )
    place_coordinates_type: list[str] | str | None = Field(None,
        description="The locating system used to describe the coordinates of a Place.",
    )


class PlaceFeature(MDSModel):
    value: Annotated[str | None, ControlledVocab] = None

    place_feature_date: Date | DateStringISO | None = Field(None,
        description="The date of the Place feature.",
    )
    place_feature_type: ControlledVocabField = Field(None,
        description="The nature or category of Place feature recorded.",
    )
