# Generated by Django 5.0 on 2023-12-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="email",
            field=models.EmailField(default="No Email", max_length=254),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_number",
            field=models.CharField(editable=False, max_length=6, unique=True),
        ),
    ]
