from uuid import UUID

from infra.event_store.aggregate_root import AggregateRoot

from .events import CustomerRegistered


class Customer(AggregateRoot):
    uid: UUID
    name: str

    def register(self, name):
        self.apply(CustomerRegistered(self.uid, name))

    def apply_customer_registered(self, event):
        self.name = event.name

    def stream_name(self, uid) -> str:
        return f"Customer#{uid}"
