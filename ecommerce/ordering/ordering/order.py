from infra.event_store.aggregate_root import AggregateRoot

from .events import ItemAddedToBasket


class Order(AggregateRoot):
    def add_item(self, product_id):
        self.apply(ItemAddedToBasket(order_id=self.uid, product_id=product_id))

    def apply_item_added_to_basket(self, event):
        pass

    def stream_name(self) -> str:
        return f"Ordering#{self.uid}"
