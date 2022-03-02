from django.db import models


class Event(models.Model):
    stream = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    data = models.TextField()
