# Generated by Django 5.0 on 2023-12-27 23:15

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0020_order_order_open"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="order",
            managers=[
                ("connected", django.db.models.manager.Manager()),
            ],
        ),
    ]
