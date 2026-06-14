from __future__ import annotations

from typing import Annotated

from pydantic import Field

from .address import Address
from .common import ControlledVocab, ControlledVocabField, MDSModel
from .date import Date, DateStringISO


class Location(MDSModel):
    value: Annotated[str | None, ControlledVocab] = None

    location_reference_name_number: list[str] | str | None = Field(None,
        description="A unique name, number, or identifier for a display or storage Location. It can also apply to a "
            "Location on a computer system used for digital objects.",
    )
    location_type: ControlledVocabField = Field(None,
        description="The nature or category of a Location.",
    )
    location_address: list[Address | str] | Address | str | None = Field(None,
        description="The address of a Location where it is not to be found on the main site of an organisation.",
    )
    location_access_note: list[str] | str | None = Field(None,
        description="Information about the access to a specific Location.",
    )
    location_condition_note: list[LocationConditionNote | str] | LocationConditionNote | str | None = Field(None,
        description="Information about the condition of the location, including such as the environmental conditions "
            "or state of cleanliness.",
    )
    location_security_note: list[str] | str | None = Field(None,
        description="Information about the security of a specific Location.",
    )
    environment_measurement_type: ControlledVocabField = Field(None,
        description="The type of environment condition measured at a location.",
    )
    environment_measurement_value: list[EnvironmentMeasurementValue | float | int] | EnvironmentMeasurementValue | float | int | None = Field(None,
        description="The numeric value of an environment measurement at a location.",
    )
    environment_measurement_date: Date | DateStringISO | None = Field(None,
        description="The date on which an environment measurement took place at a location.",
    )


class LocationConditionNote(MDSModel):
    value: str | None = None

    location_condition_note_date: Date | DateStringISO | None = Field(None,
        description="The date on which Location condition note was recorded.",
    )


class EnvironmentMeasurementValue(MDSModel):
    value: float | int | None = None

    environment_measurement_value_unit: Annotated[str | None, ControlledVocab] = Field(None,
        description="The unit of measurement used when measuring an aspect of a location's environment.",
    )
    environment_measurement_value_qualifier: Annotated[str | None, ControlledVocab] = Field(None,
        description="The measurement of accuracy used when measuring an aspect of a location's environment.",
    )
