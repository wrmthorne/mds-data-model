from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from .common import ControlledTerm, MDSModel, OneOrMany

if TYPE_CHECKING:
    from .address import Address
    from .date import Date, DateStringISO
    from .place import Place


class Person(MDSModel):
    value: str | None = None

    persons_reference_number: OneOrMany[str] = Field(
        None,
        description="A code identifying a Person associated with an object.",
    )
    persons_forenames: OneOrMany[str] = Field(
        None,
        description="A Person's given name.",
    )
    persons_surname: OneOrMany[str] = Field(
        None,
        description="A Person's family name.",
    )
    persons_title: OneOrMany[str] = Field(
        None,
        description="The form of address used by a Person.",
    )
    persons_additions_to_name: OneOrMany[str] = Field(
        None,
        description="Terms of honour used when the Person is referred to in relation to their position or work.",
    )
    persons_initials: OneOrMany[str] = Field(
        None,
        description="The initial letters of the Person's forenames and Person's surnames.",
    )
    persons_salutation: OneOrMany[str] = Field(
        None,
        description="The form of greeting used in correspondence.",
    )
    persons_address: OneOrMany[Address | str] = Field(
        None,
        description="The address where a Person can be contacted.",
    )
    persons_birth_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which a Person was born.",
    )
    persons_place_of_birth: OneOrMany[Place | str] = Field(
        None,
        description="The Place where a Person was born.",
    )
    persons_death_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which a Person died.",
    )
    persons_place_of_death: OneOrMany[Place | str] = Field(
        None,
        description="The Place where a Person died.",
    )
    persons_biographical_note: OneOrMany[str] = Field(
        None,
        description="Information about the personal history of a Person.",
    )
    persons_gender: OneOrMany[ControlledTerm] = Field(
        None,
        description="The sex of a Person.",
    )
    persons_association: OneOrMany[ControlledTerm] = Field(
        None,
        description="The way in which a Person is associated with a particular object.",
    )
    persons_group: OneOrMany[ControlledTerm] = Field(
        None,
        description="The group (social, ethnic, cultural, faith, gender orientation) to which a Person belongs or "
        "which he/she identifies him/herself.",
    )
    persons_name_notes: OneOrMany[str] = Field(
        None,
        description="A note primarily for documentation purposes to explain why the particular form of name was "
        "chosen; notes to distinguish this Person from others with the same name.",
    )
    persons_nationality: OneOrMany[ControlledTerm] = Field(
        None,
        description="A Person's official current nationality.",
    )
    persons_occupation: OneOrMany[ControlledTerm] = Field(
        None,
        description="The occupation or employment of a Person.",
    )
    persons_school_style: OneOrMany[ControlledTerm] = Field(
        None,
        description="The primary styles in which the Person worked.",
    )
