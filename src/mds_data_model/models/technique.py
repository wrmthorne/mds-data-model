from __future__ import annotations

from pydantic import Field

from .common import ControlledTerm, MDSModel, OneOrMany


class Technique(MDSModel):
    value: ControlledTerm | None = None

    technique_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the nature of the Technique.",
    )
