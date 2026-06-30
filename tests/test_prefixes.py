from __future__ import annotations

import pytest
from pydantic import ValidationError

from mds_data_model.models.address import Address
from mds_data_model.models.license import License
from mds_data_model.models.object import Object


def test_spectrum_prefix_is_the_default() -> None:
    address = Address.model_validate({"spectrum/value": "home", "spectrum/address_postcode": "S1 1AA"})
    dumped = address.model_dump(by_alias=True, exclude_none=True)
    assert dumped == {"spectrum/value": "home", "spectrum/address_postcode": "S1 1AA"}


def test_license_model_uses_ciim_prefix() -> None:
    lic = License.model_validate(
        {"ciim/value": "CC-BY", "ciim/license_url": "https://creativecommons.org/licenses/by/4.0/"}
    )
    dumped = lic.model_dump(by_alias=True)
    assert dumped["ciim/value"] == "CC-BY"
    assert str(dumped["ciim/license_url"]) == "https://creativecommons.org/licenses/by/4.0/"


def test_license_rejects_spectrum_prefixed_keys() -> None:
    """The ciim/ model should not accept the default spectrum/ prefix for required fields."""
    with pytest.raises(ValidationError):
        License.model_validate({"spectrum/value": "CC-BY", "spectrum/license_url": "https://x.org/"})


def test_object_license_field_is_overridden_to_ciim() -> None:
    assert Object.model_fields["license"].alias == "ciim/license"


def test_object_mixes_prefixes_in_one_model() -> None:
    obj = Object.model_validate(
        {
            "spectrum/object_name": "vase",
            "spectrum/object_number": "X.1",
            "ciim/license": {"ciim/value": "CC0", "ciim/license_url": "https://example.org/cc0/"},
        }
    )
    dumped = obj.model_dump(by_alias=True, exclude_none=True)
    assert "spectrum/object_name" in dumped
    assert "ciim/license" in dumped
    assert dumped["ciim/license"]["ciim/value"] == "CC0"


def test_populate_by_name_round_trip() -> None:
    """Construction and validation by Python field name must still work."""
    by_name = Object(
        object_name="vase",
        object_number="X.1",
        license=License(value="CC0", license_url="https://example.org/cc0/"),
    )
    assert by_name.object_number == "X.1"

    from_dict = Object.model_validate(
        {
            "object_name": "vase",
            "object_number": "X.1",
            "license": {"value": "CC0", "license_url": "https://example.org/cc0/"},
        }
    )
    assert from_dict.object_name == "vase"
    # Dumping without by_alias yields the Python field names.
    assert set(from_dict.model_dump(exclude_none=True)) >= {"object_name", "object_number", "license"}
