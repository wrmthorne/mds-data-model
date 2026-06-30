from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from .common import ControlledTerm, MDSModel, OneOrMany

if TYPE_CHECKING:
    from .address import Address
    from .date import Date, DateStringISO
    from .person import Person
    from .place import Place


class Organisation(MDSModel):
    value: str | None = None

    organisations_reference_number: OneOrMany[str] = Field(
        None,
        description="A code identifying an Organisation associated with an object.",
    )
    organisations_address: OneOrMany[Address | str] = Field(
        None,
        description="The address where an Organisation can be contacted.",
    )
    organisations_additions_to_name: OneOrMany[str] = Field(
        None,
        description="Additional information about the identity of an Organisation.",
    )
    organisations_contact_name: OneOrMany[Person | str] = Field(
        None,
        description="The representative of an Organisation who is normally liaised with.",
    )
    organisations_foundation_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which an Organisation formally came into being.",
    )
    organisations_foundation_place: OneOrMany[Place | str] = Field(
        None,
        description="Information about the place where an Organisation came into being.",
    )
    organisations_dissolution_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which an Organisation formally ceased to be. This may be the date on which it was "
        "taken over or wound up.",
    )
    organisations_function: OneOrMany[ControlledTerm] = Field(
        None,
        description="The activities which make up the main business of an Organisation.",
    )
    organisations_group: OneOrMany[ControlledTerm] = Field(
        None,
        description="The social, socio professional, ethnic, or culture group to which the Organisation belongs.",
    )
    organisations_history: OneOrMany[str] = Field(
        None,
        description="Information about the history of the Organisation.",
    )
    organisations_mda_code: OneOrMany[str] = Field(
        None,
        description="The code uniquely identifying an Organisation. The MDA Code system is managed by "
        "Collections Trust in the UK.",
    )
    organisations_main_body: OneOrMany[str] = Field(
        None,
        description="The name of an Organisation.",
    )
    organisations_sub_body: OneOrMany[str] = Field(
        None,
        description="The name of the sub-body of an Organisation.",
    )
    organisations_association: OneOrMany[ControlledTerm] = Field(
        None,
        description="The way in which an Organisation is associated with an object.",
    )
