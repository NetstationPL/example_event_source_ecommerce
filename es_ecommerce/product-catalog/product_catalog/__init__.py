__version__ = "0.1.0"

from infra import command_bus

from product_catalog.commands import RegisterProduct
from product_catalog.registration import Registration

command_bus.register(RegisterProduct, Registration(None))
