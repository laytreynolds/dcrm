# Generated by Django 5.0 on 2023-12-28 10:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0021_alter_order_managers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"default_manager_name": "objects", "ordering": ["-order_Created"]},
        ),
        migrations.AlterModelManagers(
            name="order",
            managers=[],
        ),
    ]
