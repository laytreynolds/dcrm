# Generated by Django 5.0 on 2023-12-27 19:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0014_alter_order_order_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_Number",
        ),
    ]
