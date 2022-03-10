import uuid

from django.db import models


class Customer(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
