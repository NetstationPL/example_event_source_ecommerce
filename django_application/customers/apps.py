from crm import configure
from django.apps import AppConfig

from infra.cqrs import cqrs


class CustomersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "customers"

    def ready(self):
        from infra.event_store.django_event_store.repository import DjangoRepository

        configure(cqrs)
        cqrs.set_repository(DjangoRepository())
