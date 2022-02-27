from unittest.mock import Mock

from infra.cqrs import CQRS
from infra.event_store import Event


class DummyEvent(Event):
    pass


def test_cqrs_publish_event():
    event_store = Mock()
    cqrs = CQRS(event_store)
    event = DummyEvent()

    cqrs.publish(event)

    event_store.publish.assert_called_with(event)


def test_cqrs_subscribe_to_event():
    event_store = Mock()
    cqrs = CQRS(event_store)
    event = DummyEvent()
    handler = Mock()

    cqrs.subscribe(handler, event)

    event_store.subscribe.assert_called_with(handler, event)