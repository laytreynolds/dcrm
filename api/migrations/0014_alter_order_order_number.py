# Generated by Django 5.0 on 2023-12-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_alter_order_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_Number",
            field=models.CharField(default="", max_length=255, unique=True),
        ),
    ]