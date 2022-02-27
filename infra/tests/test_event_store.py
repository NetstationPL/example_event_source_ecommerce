from dataclasses import dataclass
from unittest.mock import Mock
from infra.event_store import EventStore, Event


@dataclass
class ExampleEvent(Event):
    name = "Some name"


def test_should_save_event():
    repositoty = Mock()

    event_store = EventStore(repositoty)
    event = ExampleEvent()
    event_store.publish(event)

    repositoty.save.assert_called_once_with(event)


def test_should_send_events_to_subscribers():
    repositoty = Mock()
    subscriber = Mock()

    event_store = EventStore(repositoty)
    event_store.subscribe(subscriber, ExampleEvent)

    event = ExampleEvent()
    event_store.publish(event)

    subscriber.assert_called_once_with(event)
