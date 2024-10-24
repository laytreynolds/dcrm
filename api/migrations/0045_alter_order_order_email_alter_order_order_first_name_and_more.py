# Generated by Django 5.0 on 2024-01-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0044_order_order_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_Email",
            field=models.EmailField(default="", max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_First_Name",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_Last_Name",
            field=models.CharField(default="", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_Mobile",
            field=models.CharField(default="", max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_campaign",
            field=models.CharField(default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_spend_cap",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
