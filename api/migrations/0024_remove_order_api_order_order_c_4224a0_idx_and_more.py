# Generated by Django 5.0 on 2023-12-30 01:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0023_alter_order_order_open"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="order",
            name="api_order_order_C_4224a0_idx",
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["order_Mobile"], name="api_order_order_M_eb423d_idx"
            ),
        ),
    ]
