from unittest.mock import Mock

from infra.cqrs import CQRS
from infra.event_store import Event


class DummyEvent(Event):
    pass


def test_cqrs_publish_event():
    event_store = Mock()
    cqrs = CQRS(event_store)
    event = DummyEvent()
    stream_name = "stream"

    cqrs.publish(event, stream_name)

    event_store.publish.assert_called_with(event, stream_name)


def test_cqrs_subscribe_to_event():
    event_store = Mock()
    cqrs = CQRS(event_store)
    event = DummyEvent()
    handler = Mock()

    cqrs.subscribe(handler, event)

    event_store.subscribe.assert_called_with(handler, event)


def test_cqrs_return_events_from_stream():
    event_store = Mock()
    cqrs = CQRS(event_store)
    event = DummyEvent()
    event_store.read_stream.return_value = [event]

    events = cqrs.all_events_from_stream("stream")

    assert events == [event]
