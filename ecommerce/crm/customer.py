from infra.event_store.aggregate_root import AggregateRoot

from .events import CustomerRegistered


class Customer(AggregateRoot):
    def __init__(self, uid):
        super().__init__(uid)
        self.name = None

    def register(self, name):
        self.apply(CustomerRegistered(self.uid, name))

    def apply_customer_registered(self, event):
        self.name = event.name

    def stream_name(self, uid) -> str:
        return f"Customer#{uid}"
