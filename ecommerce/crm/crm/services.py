from typing import cast

from infra.event_store.aggregate_root import AggregateRootRepository

from .commands import RegisterCustomer
from .customer import Customer


class RegisterCustomerHandler:
    def __init__(self, event_store) -> None:
        self.event_store = event_store
        self.repository = AggregateRootRepository(event_store)

    def handle(self, command: RegisterCustomer) -> None:
        with self.repository.with_aggregate(Customer, command.customer_id) as customer:
            cast(Customer, customer).register(command.name)
