from __future__ import annotations

import importlib
import pkgutil

import pytest
from pydantic import BaseModel, ValidationError

import mds_data_model.models as models_pkg
from mds_data_model.models.address import Address
from mds_data_model.models.license import License
from mds_data_model.models.object import Object


def _all_model_classes() -> list[type[BaseModel]]:
    classes: dict[type[BaseModel], None] = {}
    for module_info in pkgutil.iter_modules(models_pkg.__path__):
        module = importlib.import_module(f"{models_pkg.__name__}.{module_info.name}")
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, BaseModel) and obj is not BaseModel:
                classes[obj] = None
    return list(classes)


def test_every_model_module_imports() -> None:
    for module_info in pkgutil.iter_modules(models_pkg.__path__):
        importlib.import_module(f"{models_pkg.__name__}.{module_info.name}")


@pytest.mark.parametrize("model", _all_model_classes(), ids=lambda m: m.__name__)
def test_every_model_is_fully_defined(model: type[BaseModel]) -> None:
    """Forward references are resolved for every model in the package."""
    assert model.__pydantic_complete__ is True


def test_object_validates_minimal_payload() -> None:
    obj = Object.model_validate(
        {
            "spectrum/object_name": "vase",
            "spectrum/object_number": "X.1",
            "ciim/license": {
                "ciim/value": "CC-BY",
                "ciim/license_url": "https://creativecommons.org/licenses/by/4.0/",
            },
        }
    )
    assert obj.object_number == "X.1"
    assert isinstance(obj.license, License)


def test_object_resolves_deeply_nested_cross_module_models() -> None:
    """owner -> Organisation -> Address spans three modules with cyclic refs."""
    obj = Object.model_validate(
        {
            "spectrum/object_name": "vase",
            "spectrum/object_number": "X.1",
            "ciim/license": {"ciim/value": "CC0", "ciim/license_url": "https://example.org/cc0/"},
            "spectrum/owner": {
                "spectrum/organisations_main_body": "Museum",
                "spectrum/organisations_address": {"spectrum/value": "1 High St"},
            },
        }
    )
    assert obj.owner.organisations_main_body == "Museum"
    assert obj.owner.organisations_address.value == "1 High St"


def test_missing_required_fields_raise() -> None:
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        Object.model_validate({"spectrum/object_name": "vase"})  # missing object_number + license


def test_address_uses_email_validator() -> None:
    """Address.address_email is an EmailStr, requiring the email-validator extra."""
    with pytest.raises(ValidationError):
        Address.model_validate({"spectrum/address_email": "not-an-email"})
    ok = Address.model_validate({"spectrum/address_email": "a@b.com"})
    assert str(ok.address_email) == "a@b.com"
