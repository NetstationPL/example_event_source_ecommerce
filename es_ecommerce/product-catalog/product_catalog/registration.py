from infra.command_bus import CommandHandler


from product_catalog.commands import RegisterProduct
from product_catalog.events import ProductRegistered


class Registration(CommandHandler):
    def __init__(self, cqrs):
        self.cqrs = cqrs

    def handle(self, command: RegisterProduct) -> None:
        event = ProductRegistered(product_id=command.product_id, name=command.name)

        self.cqrs.publish(event)
