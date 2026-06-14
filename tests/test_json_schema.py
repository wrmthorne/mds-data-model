"""Guard that the committed JSON Schema stays in sync with the model."""

from __future__ import annotations

from pathlib import Path

from mds_data_model.schema import build_object_schema, dumps

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "object.schema.json"

REGENERATE_HINT = "regenerate with `uv run python scripts/generate_json_schema.py`"


def test_committed_schema_exists() -> None:
    assert SCHEMA_PATH.exists(), f"{SCHEMA_PATH} is missing; {REGENERATE_HINT}"


def test_committed_schema_is_up_to_date() -> None:
    expected = dumps(build_object_schema())
    assert SCHEMA_PATH.read_text(encoding="utf-8") == expected, (
        f"Committed schema is stale; {REGENERATE_HINT}"
    )


def test_schema_uses_prefixed_property_names() -> None:
    schema = build_object_schema()
    assert schema["$schema"].endswith("2020-12/schema")
    assert "ciim/license" in schema["properties"]
    assert "spectrum/object_number" in schema["properties"]