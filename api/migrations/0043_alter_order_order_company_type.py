# Generated by Django 5.0 on 2024-01-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0042_alter_order_order_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_company_type",
            field=models.CharField(
                choices=[
                    ("SOT", "Sole Trader"),
                    ("LTD", "Limited Company"),
                    ("LTP", "Limited Partnership"),
                    ("PAR", "Partnership"),
                    ("LLP", "Limited liability Partnership"),
                    ("CHA", "Charity"),
                ],
                default="",
                max_length=20,
                null=True,
            ),
        ),
    ]
