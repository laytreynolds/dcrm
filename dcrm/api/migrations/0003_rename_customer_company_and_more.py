# Generated by Django 5.0 on 2023-12-27 13:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_customer_email_alter_order_order_number"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Customer",
            new_name="Company",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="customer",
            new_name="company",
        ),
    ]
