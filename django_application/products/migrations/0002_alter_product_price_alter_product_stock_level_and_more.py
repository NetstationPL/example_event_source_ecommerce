# Generated by Django 4.0.2 on 2022-02-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=8, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock_level",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="vat_rate_code",
            field=models.IntegerField(
                blank=True,
                choices=[(0, "0%"), (5, "5%"), (8, "8%"), (23, "23%")],
                null=True,
            ),
        ),
    ]
