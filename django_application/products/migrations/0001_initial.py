# Generated by Django 4.0.2 on 2022-02-21 19:05

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("stock_level", models.IntegerField(default=0)),
                ("registered_at", models.DateTimeField(auto_now_add=True)),
                (
                    "vat_rate_code",
                    models.IntegerField(
                        choices=[(0, "0%"), (5, "5%"), (8, "8%"), (23, "23%")]
                    ),
                ),
            ],
        ),
    ]