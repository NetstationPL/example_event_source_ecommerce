import uuid
from unittest.mock import MagicMock

from ordering.commands import AddItemToBasket, RemoveItemFromBasket
from ordering.events import ItemAddedToBasket, ItemRemovedFromBasket
from ordering.handlers import AddItemToBasketHandler, RemoveItemFromBasketHandler


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


def test_remove_item_from_basket_command_should_emit_event():
    event_store = MagicMock()
    handler = RemoveItemFromBasketHandler(event_store)
    product_id = uuid.uuid4()
    order_id = uuid.uuid4()

    handler.handle(
        RemoveItemFromBasket(
            order_id=order_id,
            product_id=product_id,
        )
    )

    event_store.publish.assert_called_once_with(
        ItemRemovedFromBasket(order_id=order_id, product_id=product_id),
        f"Ordering#{order_id}",
    )
