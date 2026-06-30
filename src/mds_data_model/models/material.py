from __future__ import annotations

from pydantic import Field

from .common import ControlledTerm, MDSModel, OneOrMany
from .place import Place


class Material(MDSModel):
    value: ControlledTerm | None = None

    material_component: OneOrMany[ControlledTerm] = Field(
        None,
        description="A significant component, inclusion or trace in the material of which an object or specimen is "
        "made. This could also include a patina or corrosion product which has developed on an object and is of "
        "sufficient significance to require documenting.",
    )
    material_component_note: OneOrMany[str] = Field(
        None,
        description="To record further information about a Material component.",
    )
    material_name: OneOrMany[str] = Field(
        None,
        description="The name commonly used to designate a particular or characteristic material, and "
        "additional to or further defining the basic material itself. This may be the vernacular or generally "
        "used name for a certain type of material or a brand name.",
    )
    material_source: OneOrMany[Place | str] = Field(
        None,
        description="The geographical origin of naturally occurring vegetable, animal or geological materials "
        "which either have been used to form an object or form specimens or deposits in their own right eg a "
        "quarry source for stone, country of origin of timber, geological outcrop for imported stone or fossil. "
        "(Note that this is separate from Object production place which is where the original materials are "
        "modified by human intervention to form an object).",
    )
