# Generated by Django 4.0.3 on 2022-03-04 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_price_alter_product_stock_level_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="vat_rate_code",
            new_name="vat_rate",
        ),
    ]
