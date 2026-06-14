"""MDS data model package.

Combined with __future__.annotations (every annotation is a string), Pydantic cannot resolve those forward references
on its own. This module imports every model, assembles one namespace containing all model classes and the shared type
aliases, and rebuilds each model against it so the whole graph is usable after a plain import mds_data_model.models.
"""

from __future__ import annotations

from pydantic import BaseModel

from . import (
    acquisition,
    address,
    common,
    date,
    dimension,
    inscription_content,
    license,
    location,
    material,
    object,
    organisation,
    people,
    person,
    place,
    reference,
    technique,
)
from .common import MDSModel

_MODULES = (
    acquisition,
    address,
    common,
    date,
    dimension,
    inscription_content,
    license,
    location,
    material,
    object,
    organisation,
    people,
    person,
    place,
    reference,
    technique,
)


def _resolve_forward_references() -> None:
    """Collect every model class plus shared aliases and rebuild against them."""
    namespace: dict[str, object] = {}
    models: list[type[BaseModel]] = []
    for module in _MODULES:
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, BaseModel):
                namespace[name] = obj
                if obj not in (BaseModel, MDSModel):
                    models.append(obj)

    # Type aliases / annotation markers that appear in field annotations but are
    # not models, so they must be resolvable without being rebuilt themselves.
    namespace["DateStringISO"] = date.DateStringISO
    namespace["ControlledVocabField"] = common.ControlledVocabField
    namespace["ControlledVocab"] = common.ControlledVocab

    for model in dict.fromkeys(models):  # de-duplicate, preserve order
        # _types_namespace supplies the cross-module names that each model's
        # own module namespace is missing.
        model.model_rebuild(_types_namespace=namespace)


_resolve_forward_references()
