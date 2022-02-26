from typing import Protocol, Type


class NoRegisteredHandlerException(Exception):
    pass


class Command:
    pass


class CommandHandler(Protocol):
    def handle(self, command: Command) -> None:
        pass


class CommandBus:
    def __init__(self):
        self.handlers = {}

    def call(self, command):
        if command.__class__ not in self.handlers:
            raise NoRegisteredHandlerException()
        self.handlers[command.__class__].handle(command)

    def register(self, command: Type[Command], handler: CommandHandler):
        self.handlers[command] = handler

    def clear_registry(self):
        self.handlers = {}
