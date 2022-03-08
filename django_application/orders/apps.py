from django.apps import AppConfig
from ordering import configure

from infra.cqrs import cqrs


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        configure(cqrs)
