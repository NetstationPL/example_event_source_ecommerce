from infra import command_bus

from product_catalog.commands import RegisterProduct


class RegisterProductHandler:
    pass


command_bus.register(RegisterProduct, RegisterProductHandler)
