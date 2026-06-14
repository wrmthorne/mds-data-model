from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import EmailStr, Field

from .common import MDSModel

if TYPE_CHECKING:
    from .common import ControlledVocab
    from .place import Place


class Address(MDSModel):
    value: str | None = None

    address_text: list[str] | None = Field(None,
        description="The address of an Organisation, Person or Location as expressed for mailing purposes.",
    )
    address_place: list[Place | str] | Place | str | None = Field(None,
        description="The elements of an Address which are required for retrieval purposes.",
    )
    address_postcode: list[str] | str | None = Field(None,
        description="The postcode or zip code of an Address.",
    )
    address_email: list[EmailStr] | EmailStr | None = Field(None,
        description="The e-mail address used to contact an Organisation or Person.",
    )
    address_fax_number: str | None = Field(None,
        description="The fax number used to contact an Organisation or Person.",
    )
    address_telephone_number: str | None = Field(None,
        description="The telephone number used to contact an Organisation or Person.",
    )
    address_type: Annotated[str | None, ControlledVocab] = Field(None,
        description="The status or use of the Address recorded.",
    )
