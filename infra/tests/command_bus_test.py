from unittest.mock import Mock

from infra import command_bus
from infra.command_bus import Command


class DummyCommand(Command):
    pass


def test_should_call_registered_handler():
    handler = Mock()
    command = DummyCommand()

    command_bus.register(DummyCommand, handler)
    command_bus.call(command)

    handler.handle.assert_called_once_with(command)
