# Generated by Django 4.0.3 on 2022-03-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_rename_vat_rate_code_product_vat_rate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="id",
            new_name="uid",
        ),
        migrations.AlterField(
            model_name="product",
            name="vat_rate",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
