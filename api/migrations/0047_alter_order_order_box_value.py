# Generated by Django 5.0 on 2024-01-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0046_alter_order_order_connection_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_box_value",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
