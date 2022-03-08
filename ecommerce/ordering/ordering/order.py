from typing import Dict
from uuid import UUID

from infra.event_store.aggregate_root import AggregateRoot

from .events import ItemAddedToBasket, ItemRemovedFromBasket


class Order(AggregateRoot):
    class Basket:
        order_lines: Dict[UUID, int]

        def __init__(self) -> None:
            self.order_lines = {}

        def increase_quantity(self, product_id: UUID) -> None:
            self.order_lines[product_id] = self.quantity(product_id) + 1

        def decrease_quantity(self, product_id: UUID) -> None:
            self.order_lines[product_id] = self.quantity(product_id) - 1

        def quantity(self, product_id: UUID) -> int:
            return self.order_lines.get(product_id, 0)

    basket: Basket

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self.basket = Order.Basket()

    def add_item(self, product_id):
        self.apply(ItemAddedToBasket(order_id=self.uid, product_id=product_id))

    def remove_item(self, product_id):
        self.apply(ItemRemovedFromBasket(order_id=self.uid, product_id=product_id))

    def apply_item_added_to_basket(self, event):
        self.basket.increase_quantity(product_id=event.product_id)

    def apply_item_removed_from_basket(self, event):
        self.basket.decrease_quantity(product_id=event.product_id)

    def stream_name(self) -> str:
        return f"Ordering#{self.uid}"
