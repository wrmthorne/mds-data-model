from __future__ import annotations

import json
from typing import Any

from .models.object import Object

JSON_SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"


def build_object_schema() -> dict[str, Any]:
    """Return the JSON Schema for :class:`Object`, keyed by external names."""
    schema = Object.model_json_schema(by_alias=True)
    # Prepend the dialect so consumers/validators know how to interpret it.
    return {"$schema": JSON_SCHEMA_DIALECT, **schema}


def dumps(schema: dict[str, Any]) -> str:
    """Serialize a schema deterministically (stable diffs, trailing newline)."""
    return json.dumps(schema, indent=2, ensure_ascii=False) + "\n"
