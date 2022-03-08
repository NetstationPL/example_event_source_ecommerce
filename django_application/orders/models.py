from django.db import models


class Order(models.Model):
    pass


class OrderLine(models.Model):
    order_id = models.UUIDField()
    product_id = models.UUIDField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
