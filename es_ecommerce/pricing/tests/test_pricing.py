from decimal import Decimal
from unittest.mock import MagicMock
from uuid import uuid1
from pricing.commands import SetPrice
from pricing.events import PriceSet
from pricing.services import SetPriceHandler


def test_set_price_should_emit_event():
    event_store = MagicMock()

    uid = uuid1()
    command = SetPrice(product_id=uid, price=Decimal(12.34))

    SetPriceHandler(event_store).handle(command)

    event_store.publish.assert_called_once_with(
        PriceSet(product_id=uid, price=12.34), f"Pricing#{uid}"
    )
