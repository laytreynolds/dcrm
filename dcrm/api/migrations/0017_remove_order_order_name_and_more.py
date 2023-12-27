# Generated by Django 5.0 on 2023-12-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0016_order_order_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_Name",
        ),
        migrations.AddIndex(
            model_name="company",
            index=models.Index(
                fields=["company_Monthly_Spend"], name="api_company_company_3cf3f6_idx"
            ),
        ),
    ]
