# Generated by Django 5.0 on 2024-01-02 20:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0035_remove_order_order_account_holder_mobile_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_name",
        ),
    ]