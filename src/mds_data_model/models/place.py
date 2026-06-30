from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from .common import ControlledTerm, MDSModel, OneOrMany

if TYPE_CHECKING:
    from .date import Date, DateStringISO
    from .organisation import Organisation
    from .people import People
    from .person import Person


class Place(MDSModel):
    value: str | None = None

    place_reference_number: OneOrMany[PlaceReferenceNumber | str] = Field(
        None,
        description="A code describing a Place associated with an object, excavation or specimen.",
    )
    place_name: OneOrMany[PlaceName | str] = Field(
        None,
        description="The name or title by which the Place is normally known.",
    )
    place_association: OneOrMany[ControlledTerm] = Field(
        None,
        description="The way in which a Place is associated with the object.",
    )
    place_context: OneOrMany[PlaceContext | str] = Field(
        None,
        description="A number, code or term identifying physical evidence of an archaeological event, such as a wall, "
        "pit or ditch.",
    )
    place_coordinates: OneOrMany[PlaceCoordinates | str] = Field(
        None,
        description="The precise location of a place expressed according to a chosen system.",
    )
    place_environmental_details: OneOrMany[str] = Field(
        None,
        description="Environmental information relevant to an object, such as details about preservation conditions "
        "of the surrounding matrix.",
    )
    place_feature: OneOrMany[PlaceFeature | str] = Field(
        None,
        description="The name by which a feature associated with an object is normally known.",
    )
    place_note: OneOrMany[str] = Field(
        None,
        description="Additional information about Place which has not been recorded elsewhere using controlled "
        "terminology.",
    )
    place_owner: OneOrMany[Organisation | People | Person | str] = Field(
        None,
        description="The owner of a Place associated with an object.",
    )
    place_position: OneOrMany[str] = Field(
        None,
        description="A precise position in a Place, usually to record the finding of an object in field collection.",
    )
    place_status: OneOrMany[ControlledTerm] = Field(
        None,
        description="A formal administrative or scientific status assigned to a Place.",
    )
    place_type_system: OneOrMany[str] = Field(
        None,
        description="The classification system from which the Place feature type is taken.",
    )


class PlaceReferenceNumber(MDSModel):
    value: str | None = None

    place_reference_number_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The category of Place reference number recorded.",
    )


class PlaceName(MDSModel):
    value: str | None = None

    place_name_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The nature or category of Place recorded.",
    )


class PlaceContext(MDSModel):
    value: str | None = None

    place_context_date: Date | DateStringISO | None = Field(
        None,
        description="The date of a context.",
    )
    place_context_level: OneOrMany[str] = Field(
        None,
        description="A level within a context.",
    )


class PlaceCoordinates(MDSModel):
    value: str | None = None

    place_coordinates_qualifier: OneOrMany[str] = Field(
        None,
        description="The measurement of accuracy of a given for Place coordinates.",
    )
    place_coordinates_type: OneOrMany[str] = Field(
        None,
        description="The locating system used to describe the coordinates of a Place.",
    )


class PlaceFeature(MDSModel):
    value: ControlledTerm | None = None

    place_feature_date: Date | DateStringISO | None = Field(
        None,
        description="The date of the Place feature.",
    )
    place_feature_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The nature or category of Place feature recorded.",
    )
