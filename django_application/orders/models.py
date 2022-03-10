from decimal import Decimal

from django.db import models


class Order(models.Model):
    uid = models.UUIDField(primary_key=True, default=None, editable=False)

    def discounted_value(self):
        return sum(ol.value() for ol in self.orderline_set.all())


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.UUIDField()
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def value(self):
        return self.price * Decimal(self.quantity)
