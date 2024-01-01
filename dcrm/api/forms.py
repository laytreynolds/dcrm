from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class SearchForm(forms.Form):
    query = forms.CharField(label="search", max_length=100)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "company",
            "order_Title",
            "order_First_Name",
            "order_Last_Name",
            "order_Mobile",
            "order_Landline",
            "order_Email",
            "order_House_Number",
            "order_Street",
            "order_City",
            "order_County",
            "order_Postcode",
            "order_Delivery_House_Number",
            "order_Delivery_Street",
            "order_Delivery_City",
            "order_Delivery_County",
            "order_Delivery_Postcode",
            "status",
            "order_network",
            "order_name",
            "order_box_value",
            "order_deal_source",
            "order_connected_date",
            "order_loss_reason",
            "order_mobile_number",
            "order_contact_title",
            "order_contact_name",
            "order_date_of_birth",
            "order_account_holder_mobile_number",
            "order_email_address",
            "order_account_address",
            "order_campaign",
            "order_connection_type",
            "order_eligibility_date",
            "order_handset",
            "order_tariff",
            "order_sim_required",
            "order_tariff_code",
            "order_spend_cap",
            "order_network_account_number",
            "order_additional_details",
            "order_commission_details",
            "order_company_type",
        ]

        labels = {
            "company": "Company",
            "order_Title": "Title",
            "order_First_Name": "First Name",
            "order_Last_Name": "Last Name",
            "order_Mobile": "Mobile",
            "order_Landline": "Landline",
            "order_Email": "Email",
            "order_House_Number": "House Number",
            "order_Street": "Street",
            "order_City": "City",
            "order_County": "County",
            "order_Postcode": "Postcode",
            "order_Delivery_House_Number": "Delivery House Number",
            "order_Delivery_Street": "Delivery Street",
            "order_Delivery_City": "Delivery City",
            "order_Delivery_County": "Delivery County",
            "order_Delivery_Postcode": "Delivery Postcode",
            "status": "Status",
            "order_network": "Network",
            "order_name": "Name",
            "order_box_value": "Box Value",
            "order_deal_source": "Deal Source",
            "order_connected_date": "Connected Date",
            "order_loss_reason": "Loss Reason",
            "order_mobile_number": "Mobile Number",
            "order_contact_title": "Contact Title",
            "order_contact_name": "Contact Name",
            "order_date_of_birth": "Date of Birth",
            "order_account_holder_mobile_number": "Account Holder Mobile Number",
            "order_email_address": "Email Address",
            "order_account_address": "Account Address",
            "order_campaign": "Campaign",
            "order_connection_type": "Connection Type",
            "order_eligibility_date": "Eligibility Date",
            "order_handset": "Handset",
            "order_tariff": "Tariff",
            "order_sim_required": "SIM Required",
            "order_tariff_code": "Tariff Code",
            "order_spend_cap": "Spend Cap",
            "order_network_account_number": "Network Account Number",
            "order_additional_details": "Additional Details",
            "order_commission_details": "Commission Details",
            "order_Open": "Open",
            "order_company_type": "Company Type",
        }

        widgets = {
            "order_date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "order_donnected_date": forms.DateInput(attrs={"type": "date"}),
            "order_eligibility_date": forms.DateInput(attrs={"type": "date"}),
        }

        exclude = ["owner", "order_Open"]
