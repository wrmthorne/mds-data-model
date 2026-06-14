from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field
from .common import MDSModel

if TYPE_CHECKING:
    from .address import Address
    from .person import Person
    from .common import ControlledVocabField
    from .date import Date, DateStringISO
    from .place import Place


class Organisation(MDSModel):
    value: str | None = None

    organisations_reference_number: list[str] | str | None = Field(None,
        description="A code identifying an Organisation associated with an object.",
    )
    organisations_address: list[Address | str] | Address | str | None = Field(None,
        description="The address where an Organisation can be contacted.",
    )
    organisations_additions_to_name: list[str] | str | None = Field(None,
        description="Additional information about the identity of an Organisation.",
    )
    organisations_contact_name: list[Person | str] | Person | str | None = Field(None,
        description="The representative of an Organisation who is normally liaised with.",
    )
    organisations_foundation_date: Date | DateStringISO | None = Field(None,
        description="The date on which an Organisation formally came into being.",
    )
    organisations_foundation_place: list[Place | str] | Place | str | None = Field(None,
        description="Information about the place where an Organisation came into being.",
    )
    organisations_dissolution_date: Date | DateStringISO | None = Field(None,
        description="The date on which an Organisation formally ceased to be. This may be the date on which it was "
            "taken over or wound up.",
    )
    organisations_function: ControlledVocabField = Field(None,
        description="The activities which make up the main business of an Organisation.",
    )
    organisations_group: ControlledVocabField = Field(None,
        description="The social, socio professional, ethnic, or culture group to which the Organisation belongs.",
    )
    organisations_history: list[str] | str | None = Field(None,
        description="Information about the history of the Organisation.",
    )
    organisations_mda_code: list[str] | str | None = Field(None,
        description="The code uniquely identifying an Organisation. The MDA Code system is managed by "
            "Collections Trust in the UK.",
    )
    organisations_main_body: list[str] | str | None = Field(None,
        description="The name of an Organisation.",
    )
    organisations_sub_body: list[str] | str | None = Field(None,
        description="The name of the sub-body of an Organisation.",
    )
    organisations_association: ControlledVocabField = Field(None,
        description="The way in which an Organisation is associated with an object.",
    )