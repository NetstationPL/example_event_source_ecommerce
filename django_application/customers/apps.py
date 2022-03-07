from crm import configure
from crm.events import CustomerRegistered
from django.apps import AppConfig

from infra.cqrs import cqrs


class CustomersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "customers"

    def ready(self):
        from infra.event_store.django_event_store.repository import DjangoRepository

        from . import handlers

        configure(cqrs)
        cqrs.set_repository(DjangoRepository())

        cqrs.subscribe(handlers.create_customer, CustomerRegistered)
