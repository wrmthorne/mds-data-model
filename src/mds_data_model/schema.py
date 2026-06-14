"""JSON Schema generation for the MDS data model.

The schema is generated from the root :class:`Object` model and committed to the
repository (``schema/object.schema.json``) as documentation. The logic lives
here so the generator script and the drift test share one source of truth.
"""

from __future__ import annotations

import json
from typing import Any

from .models.object import Object

#: Pydantic targets this dialect but omits the ``$schema`` key from its output.
JSON_SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"


def build_object_schema() -> dict[str, Any]:
    """Return the JSON Schema for :class:`Object`, keyed by external names.

    ``by_alias=True`` makes the schema use the namespaced property names that the
    real data carries (``spectrum/...``, ``ciim/...``) rather than the Python
    field names.
    """
    schema = Object.model_json_schema(by_alias=True)
    # Prepend the dialect so consumers/validators know how to interpret it.
    return {"$schema": JSON_SCHEMA_DIALECT, **schema}


def dumps(schema: dict[str, Any]) -> str:
    """Serialize a schema deterministically (stable diffs, trailing newline)."""
    return json.dumps(schema, indent=2, ensure_ascii=False) + "\n"