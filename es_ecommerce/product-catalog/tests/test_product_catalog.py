from dataclasses import dataclass
from unittest.mock import Mock
import uuid

from product_catalog.commands import RegisterProduct
from product_catalog import Registration


@dataclass
class ProductRegistered(object):
    name: str
    product_id: uuid.UUID


def test_should_publish_event():
    cqrs = Mock()
    uid = uuid.uuid4()
    command = RegisterProduct(name="Product 1", product_id=uid)

    Registration(cqrs).handle(command)

    cqrs.publish.assert_called_once_with(
        ProductRegistered(name="Product 1", product_id=uid)
    )
