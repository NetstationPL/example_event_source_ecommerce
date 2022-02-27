from unittest.mock import MagicMock
import uuid
import pytest

from product_catalog.commands import RegisterProduct
from product_catalog.events import ProductRegistered
from product_catalog.exceptions import AlreadyRegistered
from product_catalog import Registration


def test_should_publish_event():
    cqrs = MagicMock()
    cqrs.all_events_from_stream.return_value = []
    uid = uuid.uuid4()
    command = RegisterProduct(name="Product 1", product_id=uid)

    Registration(cqrs).handle(command)

    cqrs.publish.assert_called_once_with(
        ProductRegistered(name="Product 1", product_id=uid), f"Catalog::Product#{uid}"
    )


def test_should_raise_exception_when_product_was_registered_before():
    uid = uuid.uuid4()
    cqrs = MagicMock()
    cqrs.all_events_from_stream.return_value = [
        ProductRegistered(product_id=uid, name="Some Name")
    ]
    command = RegisterProduct(name="Product 1", product_id=uid)

    with pytest.raises(AlreadyRegistered):
        Registration(cqrs).handle(command)
