from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import EmailStr, Field

from .common import ControlledTerm, MDSModel, OneOrMany

if TYPE_CHECKING:
    from .place import Place


class Address(MDSModel):
    value: str | None = None

    address_text: list[str] | None = Field(
        None,
        description="The address of an Organisation, Person or Location as expressed for mailing purposes.",
    )
    address_place: OneOrMany[Place | str] = Field(
        None,
        description="The elements of an Address which are required for retrieval purposes.",
    )
    address_postcode: OneOrMany[str] = Field(
        None,
        description="The postcode or zip code of an Address.",
    )
    address_email: OneOrMany[EmailStr] = Field(
        None,
        description="The e-mail address used to contact an Organisation or Person.",
    )
    address_fax_number: str | None = Field(
        None,
        description="The fax number used to contact an Organisation or Person.",
    )
    address_telephone_number: str | None = Field(
        None,
        description="The telephone number used to contact an Organisation or Person.",
    )
    address_type: ControlledTerm | None = Field(
        None,
        description="The status or use of the Address recorded.",
    )
