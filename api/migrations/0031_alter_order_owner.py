# Generated by Django 5.0 on 2023-12-31 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0030_rename_order_comapny_type_order_order_company_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="owner",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sales",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
