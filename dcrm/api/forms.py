from django import forms
from .models import Order, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, HTML
from crispy_forms.bootstrap import PrependedText
from django.utils.safestring import mark_safe

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'status']


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
                    Div(
                        PrependedText(
                            "status",
                            mark_safe('<i class="fa-solid fa-chart-simple"></i>'),
                        ),
                        PrependedText(
                            "order_campaign",
                            mark_safe('<i class="fa-solid fa-bullseye"></i>'),
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "order_Mobile",
                            mark_safe('<i class="fa-solid fa-mobile"></i>'),
                        ),
                        PrependedText(
                            "order_connection_type",
                            mark_safe('<i class="fa-solid fa-shopping-cart"></i>'),
                        ),
                        css_class="col-md-6",
                    ),
                    css_class="row",
                ),
                HTML("<br>"),
            ),
            Fieldset(
                "Account Information",
                Div(
                    Div(
                        PrependedText(
                            "order_Title", mark_safe('<i class="fa-solid fa-user"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "order_company_name",
                            mark_safe('<i class="fa-solid fa-briefcase"></i>'),
                        ),
                        css_class="col-md-6",
                    ),
                    Div("order_First_Name", css_class="col-md-6"),
                    Div("order_company_type", css_class="col-md-6"),
                    Div("order_Last_Name", css_class="col-md-6"),
                    Div(
                        PrependedText(
                            "order_Landline",
                            mark_safe('<i class="fa-solid fa-phone"></i>'),
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "order_Email", mark_safe('<i class="fa-solid fa-at"></i>')
                        ),
                        css_class="col-md-6",
                    ),
                    Div(
                        PrependedText(
                            "order_date_of_birth",
                            mark_safe('<i class="fa-solid fa-calendar"></i>'),
                        ),
                        css_class="col-md-6",
                    ),
                    css_class="row",
                ),
                HTML("<br>")
                # Other fields related to personal information
            ),
            Div(
                HTML("<br> <hr>"),
                Div(
                    Div(
                        css_class="col-md-9 offset-md-8",
                    ),
                    css_class="row",
                ),
                Fieldset(
                    "Billing Address",
                    Div(
                        Div(
                            PrependedText(
                                "order_House_Number",
                                mark_safe('<i class="fa-solid fa-location-dot"></i>'),
                            ),
                            css_id="order_house_number",
                        ),
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
                        Div(
                            PrependedText(
                                "order_Delivery_House_Number",
                                mark_safe('<i class="fa-solid fa-location-dot"></i>'),
                            ),
                            css_id="delivery_house_number",
                        ),
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
                        Div(
                            PrependedText(
                                "order_connection_type",
                                mark_safe('<i class="fa-solid fa-cart-shopping"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            PrependedText(
                                "order_network",
                                mark_safe('<i class="fa-solid fa-wifi"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            "order_tariff",
                            css_class="col-md-6",
                        ),
                        Div(
                            PrependedText(
                                "order_eligibility_date",
                                mark_safe('<i class="fa-solid fa-calendar"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            PrependedText(
                                "order_box_value",
                                mark_safe('<i class="fa-solid fa-sterling-sign"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            PrependedText(
                                "order_spend_cap",
                                mark_safe('<i class="fa-solid fa-sterling-sign"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            PrependedText(
                                "order_sim_required",
                                mark_safe('<i class="fa-solid fa-sim-card"></i>'),
                            ),
                            css_class="col-md-6",
                        ),
                        Div(
                            Div(
                                PrependedText(
                                    "order_commission_details",
                                    mark_safe('<i class="fa-solid fa-percent"></i>'),
                                ),
                                css_class="col-md-6",
                            ),
                            Div(
                                PrependedText(
                                    "order_additional_details",
                                    mark_safe(
                                        '<i class="fa-solid fa-circle-info"></i>'
                                    ),
                                ),
                                css_class="col-md-6",
                            ),
                            css_class="row",
                        ),
                        css_class="row",
                    ),
                    HTML("<br>"),
                    Div(
                        Submit(
                            "submit",
                            "Submit Order",
                            css_class="btn btn-success",
                        ),
                        css_class="row",
                    ),
                ),
            ),
        )

    class Meta:
        model = Order

        labels = {
            "company": "Company",
            "order_company_type": "Business Type",
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
            "order_box_value": "Box Value",
            "order_deal_source": "Deal Source",
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
            "order_sim_required": "Sim Required",
            "order_company_name": "Business Name",
        }

        widgets = {
            "order_connected_date": forms.DateInput(attrs={"type": "date"}),
            "order_date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "order_eligibility_date": forms.DateInput(attrs={"type": "date"}),
        }

        exclude = ["owner", "order_Open"]
