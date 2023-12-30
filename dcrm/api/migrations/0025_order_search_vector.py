# Generated by Django 5.0 on 2023-12-30 02:29

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0024_remove_order_api_order_order_c_4224a0_idx_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]