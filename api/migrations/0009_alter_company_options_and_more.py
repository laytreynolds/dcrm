# Generated by Django 5.0 on 2023-12-27 18:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_alter_order_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name_plural": "Companies"},
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_Name",
            new_name="name",
        ),
    ]
