from dataclasses import dataclass
from unittest.mock import Mock

from infra.event_store import Event, EventStore
from infra.repository import Repository


@dataclass
class ExampleEvent(Event):
    name = "Some name"


def test_should_save_event():
    repository = Mock()
    event_store = EventStore(repository)
    event = ExampleEvent()
    stream_name = "stream_name"

    event_store.publish(event, stream_name)

    repository.save.assert_called_once_with(event, stream_name)


def test_should_send_events_to_subscribers():
    repository = Mock()
    subscriber = Mock()

    event_store = EventStore(repository)
    event = ExampleEvent()
    stream_name = "stream_name"

    event_store.subscribe(subscriber, ExampleEvent)
    event_store.publish(event, stream_name)

    subscriber.assert_called_once_with(event)


def test_should_return_stream_of_events():
    event_store = EventStore(Repository())
    event = ExampleEvent()
    stream_name = "stream_name"

    event_store.publish(event, stream_name)

    assert event_store.read_stream(stream_name) == [event]
