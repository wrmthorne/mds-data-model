from __future__ import annotations

from pathlib import Path

from mds_data_model.schema import build_object_schema, dumps

OUTPUT = Path(__file__).resolve().parent.parent / "schema" / "object.schema.json"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(dumps(build_object_schema()), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()