import uuid

from django.db import models


class Product(models.Model):
    VAT_RATE_CHOICES = (
        (0, '0%'),
        (5, '5%'),
        (8, '8%'),
        (23, '23%'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_level = models.IntegerField(default=0)
    registered_at = models.DateTimeField(auto_now_add=True)
    vat_rate_code = models.IntegerField(choices=VAT_RATE_CHOICES)

    def __str__(self):
        return self.name
