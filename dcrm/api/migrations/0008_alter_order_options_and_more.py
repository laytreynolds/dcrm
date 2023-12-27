# Generated by Django 5.0 on 2023-12-27 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_order_owner_alter_order_company"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-order_Created"]},
        ),
        migrations.RemoveIndex(
            model_name="order",
            name="api_order_order_c_823ea9_idx",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_employees",
            new_name="company_Employees",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_monthly_spend",
            new_name="company_Monthly_spend",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_number_of_orders",
            new_name="company_Number_of_orders",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_type",
            new_name="company_Type",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="company_updated",
            new_name="company_Updated",
        ),
        migrations.RenameField(
            model_name="company",
            old_name="compapy_created",
            new_name="compapy_Created",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_city",
            new_name="order_City",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_county",
            new_name="order_County",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_created",
            new_name="order_Created",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_delivery_city",
            new_name="order_Delivery_city",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_delivery_county",
            new_name="order_Delivery_county",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_delivery_house_number",
            new_name="order_Delivery_house_number",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_delivery_post_code",
            new_name="order_Delivery_post_code",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_delivery_street",
            new_name="order_Delivery_street",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_email",
            new_name="order_Email",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_first_name",
            new_name="order_First_name",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_house_number",
            new_name="order_House_number",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_id",
            new_name="order_Id",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_landline",
            new_name="order_Landline",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_last_name",
            new_name="order_Last_name",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_mobile",
            new_name="order_Mobile",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_number",
            new_name="order_Number",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_post_code",
            new_name="order_Post_code",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_street",
            new_name="order_Street",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_title",
            new_name="order_Title",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="order_updated",
            new_name="order_Updated",
        ),
        migrations.AddField(
            model_name="company",
            name="company_Name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["order_Created"], name="api_order_order_C_4224a0_idx"
            ),
        ),
    ]
