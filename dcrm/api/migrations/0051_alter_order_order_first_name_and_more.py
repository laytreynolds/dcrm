# Generated by Django 5.0 on 2024-01-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0050_alter_order_order_first_name_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_First_Name",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_spend_cap",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
    ]
