__version__ = "0.1.0"

from infra import command_bus

from .commands import RegisterCustomer
from .services import RegisterCustomerHandler


def configure(cqrs):
    command_bus.register(RegisterCustomer, RegisterCustomerHandler(cqrs.event_store))
