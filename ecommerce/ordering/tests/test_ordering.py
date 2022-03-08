from unittest.mock import MagicMock

from ordering.commands import AddItemToBasket
from ordering.events import ItemAddedToBasket
from ordering.handlers import AddItemToBasketHandler


def test_add_item_to_basket_command_should_emit_event():
    event_store = MagicMock()
    handler = AddItemToBasketHandler(event_store)
    handler.handle(AddItemToBasket(product_id="4abc1a07-4230-4043-8964-96125c21bb05", order_id="0bfc85bd-4ee3-439d-b079-f473d0d74fb8"))
    event_store.publish.assert_called_with(
        ItemAddedToBasket(
            product_id="4abc1a07-4230-4043-8964-96125c21bb05",
            order_id="0bfc85bd-4ee3-439d-b079-f473d0d74fb8"
        )
    )
