from __future__ import annotations

from pydantic import AnyUrl, ConfigDict

from .common import MDSModel


class License(MDSModel):
    # License properties are namespaced under ``ciim/`` rather than the default
    # ``spectrum/``; override the alias generator for this model only.
    model_config = ConfigDict(
        alias_generator=lambda name: f"ciim/{name}",
        populate_by_name=True,
    )

    value: str
    license_url: AnyUrl