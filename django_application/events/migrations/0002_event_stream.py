# Generated by Django 4.0.2 on 2022-03-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='stream',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
