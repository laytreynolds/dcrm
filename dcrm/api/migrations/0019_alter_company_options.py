# Generated by Django 5.0 on 2023-12-27 20:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0018_alter_order_order_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"ordering": ["company_Name"], "verbose_name_plural": "Companies"},
        ),
    ]