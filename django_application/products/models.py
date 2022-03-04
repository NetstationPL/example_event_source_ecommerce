import uuid

from django.conf import settings
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stock_level = models.IntegerField(default=0, null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    vat_rate = models.IntegerField(
        choices=settings.AVAILABLE_VAT_RATES, null=True, blank=True
    )

    def __str__(self):
        return self.name
