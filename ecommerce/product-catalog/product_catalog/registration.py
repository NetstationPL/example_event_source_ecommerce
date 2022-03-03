from product_catalog.commands import RegisterProduct
from product_catalog.events import ProductRegistered
from product_catalog.exceptions import AlreadyRegistered

from infra.command_bus import CommandHandler
from infra.cqrs import CQRS


class Registration(CommandHandler):
    def __init__(self, cqrs: CQRS) -> None:
        self.cqrs = cqrs

    def handle(self, command: RegisterProduct) -> None:
        if self.cqrs.all_events_from_stream(self.stream_name(command)):
            raise AlreadyRegistered("Product already registered")

        event = ProductRegistered(product_id=command.product_id, name=command.name)
        self.cqrs.publish(event, self.stream_name(command))

    def stream_name(self, command: RegisterProduct) -> str:
        return f"Catalog::Product#{command.product_id}"
