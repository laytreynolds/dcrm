# Generated by Django 5.0 on 2024-01-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0045_alter_order_order_email_alter_order_order_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_connection_type",
            field=models.CharField(default="", max_length=255, null=True),
        ),
    ]