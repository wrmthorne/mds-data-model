from __future__ import annotations

from pydantic import Field

from .common import ControlledTerm, MDSModel
from .date import Date, DateStringISO


class Dimension(MDSModel):
    value: ControlledTerm | None = None

    dimension_measured_part: ControlledTerm | None = Field(
        None,
        description="The part of an object measured.",
    )
    dimension_value: DimensionValue | float | int | None = Field(
        None,
        description="The numeric value of the measurement of a Dimension.",
    )
    dimension_measurement_unit: ControlledTerm | None = Field(
        None,
        description="The unit of measurement used when measuring a Dimension.",
    )
    dimension_value_qualifier: str | None = Field(
        None,
        description="The measurement of statistical deviation given for a dimension. If left blank, the assumption is "
        "that the dimension accuracy recorded is thought to be correct. Do not use capitalisation or punctuation.",
    )


class DimensionValue(MDSModel):
    value: float | int

    dimension_value_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which the Dimension value was recorded.",
    )
