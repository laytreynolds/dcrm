# Generated by Django 5.0 on 2023-12-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "api",
            "0011_rename_company_monthly_spend_company_company_monthly_spend_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_Number",
            field=models.CharField(
                default="", editable=False, max_length=15, unique=True
            ),
        ),
    ]