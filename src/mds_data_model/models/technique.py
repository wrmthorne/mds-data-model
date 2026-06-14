from __future__ import annotations

from typing import Annotated

from pydantic import Field

from .common import ControlledVocab, ControlledVocabField, MDSModel


class Technique(MDSModel):
    value: Annotated[str | None, ControlledVocab] = None

    technique_type: ControlledVocabField = Field(None,
        description="A term describing the nature of the Technique.",
    )
