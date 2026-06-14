from __future__ import annotations

from typing import Annotated

from pydantic import Field

from .common import ControlledVocab, MDSModel

DateStringISO = Annotated[str, Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")]


class Date(MDSModel):
    value: str | None = None

    date_association: list[str] | str | None = Field(None,
        description="How a Date relates to an event in an object’s history.",
    )
    date_earliest_single: DateEarliestSingle | str | None = Field(None,
        description="The earliest probable or exact date at which an event in an object’s history is thought to have "
            "occurred.",
    )
    date_latest: DateLatest | str | None = Field(None,
        description="The latest probable date at which an event in an object’s history is thought to have occurred.",
    )
    date_period: list[str] | str | None = Field(None,
        description="A textual expression of the period when an event in an object’s history is thought to have "
            "occurred.",
    )
    date_text: list[str] | str | None = Field(None,
        description="The textual expression of the date or date span when an event in an object’s history is thought "
            "to have occurred.",
    )


class DateEarliestSingle(MDSModel):
    value: DateStringISO

    date_earliest_single_certainty: Annotated[str | None, ControlledVocab] = Field(None,
        description="A term describing the extent to which the Date – earliest/single recorded is thought to be "
            "correct.",
    )
    date_earliest_single_qualifier: Annotated[str | None, ControlledVocab] = Field(None,
        description="A qualification of the earliest probable or exact date at which an event in an object’s history "
            "is thought to have occurred.",
    )


class DateLatest(MDSModel):
    value: DateStringISO

    date_latest_certainty: Annotated[str | None, ControlledVocab] = Field(None,
        description="A term describing the extent to which the Date – latest recorded is thought to be correct.",
    )
    date_latest_qualifier: Annotated[str | None, ControlledVocab] = Field(None,
        description="A qualification of the latest probable date at which an event in the object’s history is thought "
            "to have occurred.",
    )