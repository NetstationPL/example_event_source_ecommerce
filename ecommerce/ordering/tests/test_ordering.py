import uuid
from unittest.mock import MagicMock

from ordering.commands import AddItemToBasket
from ordering.events import ItemAddedToBasket
from ordering.handlers import AddItemToBasketHandler


def test_add_item_to_basket_command_should_emit_event():
    event_store = MagicMock()
    handler = AddItemToBasketHandler(event_store)
    product_id = uuid.uuid4()
    order_id = uuid.uuid4()

    handler.handle(
        AddItemToBasket(
            order_id=order_id,
            product_id=product_id,
        )
    )

    event_store.publish.assert_called_once_with(
        ItemAddedToBasket(order_id=order_id, product_id=product_id),
        f"Ordering#{order_id}",
    )
