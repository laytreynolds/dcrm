from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, HTML, Field


class SearchForm(forms.Form):
    query = forms.CharField(label="search", max_length=100)


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    None,
                    Div("order_campaign", css_class="col-md-6"),
                    Div("order_Mobile", css_class="col-md-6"),
                    css_class="row",
                ),
                HTML("<br>"),
            ),
            Fieldset(
                "Account Information",
                Div(
                    Div("order_Title", css_class="col-md-6"),
                    Div("order_company_type", css_class="col-md-6"),
                    Div("order_First_Name", css_class="col-md-6"),
                    Div("company", css_class="col-md-6"),
                    Div("order_Last_Name", css_class="col-md-6"),
                    Div("order_Landline", css_class="col-md-6"),
                    Div("order_Email", css_class="col-md-6"),
                    Div("order_date_of_birth", css_class="col-md-6"),
                    css_class="row",
                ),
                HTML("<br>")
                # Other fields related to personal information
            ),
            Div(
                HTML("<br> <hr>"),
                Fieldset(
                    "Billing Address",
                    Div(
                        Div("order_House_Number"),
                        Div("order_Street"),
                        Div("order_City"),
                        Div("order_County"),
                        Div("order_Postcode"),
                    ),
                    css_class="address-inline",
                ),
                Fieldset(
                    "Delivery Address",
                    Div(
                        Div("order_Delivery_House_Number"),
                        Div("order_Delivery_Street"),
                        Div("order_Delivery_City"),
                        Div("order_Delivery_County"),
                        Div("order_Delivery_Postcode"),
                    ),
                    HTML("<br>"),
                    css_class="address-inline",
                ),
                HTML("<br><hr>"),
                css_class="row",
            ),
            Div(
                Fieldset(
                    "Sale Details",
                    Div(
                        Div("order_connection_type", css_class="col-md-6"),
                        Div("order_network", css_class="col-md-6"),
                        Div("order_box_value", css_class="col-md-6"),
                        Div("order_eligibility_date", css_class="col-md-6"),
                        Div("order_tariff", css_class="col-md-6"),
                        Div("order_deal_source", css_class="col-md-6"),
                        Div("order_spend_cap", css_class="col-md-6"),
                        Div("order_commission_details"),
                        Div("order_additional_details"),
                        css_class="row",
                    ),
                    HTML("<br> <hr>"),
                    Submit("submit", "Submit"),
                ),
            ),
        )

    class Meta:
        model = Order

        labels = {
            "company": "Company",
            "order_company_type": "Company Type",
            "order_Title": "Title",
            "order_First_Name": "First Name",
            "order_Last_Name": "Last Name",
            "order_Mobile": "Mobile",
            "order_Landline": "Landline",
            "order_Email": "Email",
            "order_House_Number": "House Number / Name",
            "order_Delivery_House_Number": "Delivery House Number / Name",
            "order_Delivery_Street": "Delivery Street",
            "order_Delivery_City": "Delivery City",
            "order_Delivery_County": "Delivery County",
            "order_Delivery_Postcode": "Delivery Postcode",
            "order_network": "Network",
            "order_name": "Name",
            "order_box_value": "Box Value",
            "order_deal_source": "Deal Source",
            "order_loss_reason": "Loss Reason",
            "order_Street": "Street",
            "order_City": "City",
            "order_County": "County",
            "order_Postcode": "Postcode",
            "order_date_of_birth": "Date of Birth",
            "order_campaign": "Campaign",
            "order_eligibility_date": "Eligibility Date",
            "order_connected_date": "Connected Date",
            "order_tariff": "Tariff",
            "order_connection_type": "Sale Type",
            "order_commission_details": "Commission Details",
            "order_additional_details": "Addional Details",
            "order_spend_cap": "Spend Cap",
        }

        widgets = {
            "order_connected_date": forms.DateInput(attrs={"type": "date"}),
            "order_date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "order_eligibility_date": forms.DateInput(attrs={"type": "date"}),
        }

        exclude = ["owner", "order_Open"]
