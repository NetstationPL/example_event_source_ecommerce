__version__ = "0.1.0"

from product_catalog.commands import RegisterProduct
from product_catalog.registration import Registration

from infra import command_bus


def configure(cqrs):
    command_bus.register(RegisterProduct, Registration(cqrs))
