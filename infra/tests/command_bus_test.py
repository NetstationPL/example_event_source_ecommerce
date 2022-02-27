from unittest.mock import Mock

import pytest

from infra import command_bus
from infra.command_bus import Command, NoRegisteredHandlerException


class DummyCommand(Command):
    pass


@pytest.fixture(autouse=True)
def clear_registry():
    command_bus.clear_registry()


def test_should_call_registered_handler():
    handler = Mock()
    command = DummyCommand()

    command_bus.register(DummyCommand, handler)
    command_bus.call(command)

    handler.handle.assert_called_once_with(command)


def test_should_raise_exception_if_no_handler_registered():
    command = DummyCommand()

    with pytest.raises(NoRegisteredHandlerException):
        command_bus.call(command)
