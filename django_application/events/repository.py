from infra.event_store.event_store import Event as SourceEvent
from infra.repository import Repository

from .models import Event


class DjangoRepository(Repository):
    def save(self, event: SourceEvent, stream_name: str):
        Event.objects.create(
            name=event.__class__.__name__, data=event.to_json(), stream=stream_name
        )

    def read(self, stream_name: str):
        return Event.objects.filter(stream=stream_name)

    def clear(self):
        return Event.objects.all().delete()
