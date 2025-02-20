# Generated by Django 5.0 on 2023-12-27 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_order_status_order_api_order_order_c_823ea9_idx"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="owner",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sales",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="api.company",
            ),
        ),
    ]
