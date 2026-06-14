from __future__ import annotations

from typing import Annotated

from mds_data_model.introspection import (
    _annotation_contains,
    date_fields,
    fields_of_type,
)
from mds_data_model.models.date import Date
from mds_data_model.models.object import Object
from mds_data_model.models.person import Person


class TestAnnotationContains:
    def test_matches_bare_type(self) -> None:
        assert _annotation_contains(Date, Date)

    def test_matches_inside_union(self) -> None:
        assert _annotation_contains(Date | str | None, Date)

    def test_matches_nested_in_container(self) -> None:
        assert _annotation_contains(list[Date | str], Date)

    def test_matches_inside_annotated(self) -> None:
        assert _annotation_contains(Annotated[Date | None, "meta"], Date)

    def test_does_not_match_absent_type(self) -> None:
        assert not _annotation_contains(str | None, Date)
        assert not _annotation_contains(list[str], Date)


class TestDateFields:
    def test_returns_a_tuple(self) -> None:
        assert isinstance(date_fields(), tuple)

    def test_includes_known_date_fields(self) -> None:
        fields = date_fields()
        assert "accession_date" in fields  # Date | DateStringISO | None
        assert "associated_date" in fields  # list[Date | DateStringISO] | ... | None

    def test_excludes_non_date_fields(self) -> None:
        fields = date_fields()
        assert "object_number" not in fields  # list[str] | str
        assert "object_name" not in fields

    def test_defaults_to_object_model(self) -> None:
        assert date_fields() == date_fields(Object)

    def test_model_without_date_typed_fields_returns_empty(self) -> None:
        # Date's own fields reference DateEarliestSingle / DateLatest, not Date.
        assert date_fields(Date) == ()


class TestFieldsOfType:
    def test_date_fields_delegates_to_fields_of_type(self) -> None:
        assert date_fields(Object) == fields_of_type(Object, Date)

    def test_finds_fields_of_other_types(self) -> None:
        person_fields = fields_of_type(Object, Person)
        assert "owner" in person_fields  # Organisation | People | Person | str | ...
        assert all(isinstance(name, str) for name in person_fields)

    def test_result_is_cached(self) -> None:
        assert fields_of_type(Object, Date) is fields_of_type(Object, Date)
