from django import forms
from .models import Order, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, HTML, Field
from django.forms.widgets import RadioSelect
from crispy_forms.bootstrap import PrependedText
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User



class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("body", label=""),
            Field("status", label=""),
            Submit("submit", "Submit", css_class="btn btn-primary"),
        )

    class Meta:
        model = Comment
        exclude = ['owner', 'order']
        labels = {
            'body': '',
            'status': '',
        }


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
                            "campaign",
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
            "campaign": "Campaign",
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

class OrderUpdateForm(forms.ModelForm):
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
                            "campaign",
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
                            "Update Order",
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
            "campaign": "Campaign",
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

class CreateUserForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput,
        strip=False,
        required=False,  # Make this optional for editing
        help_text="Enter the same password as above, for verification."
    )
    
    # Adding choices for is_active and is_staff fields
    ACTIVE_STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    STAFF_STATUS_CHOICES = [
        (True, 'Staff'),
        (False, 'Non-Staff'),
    ]
    
    SUPERUSER_STATUS_CHOICES = [
        (True, 'Super User'),
        (False, 'Normal User'),
    ]

    is_active = forms.ChoiceField(
        choices=ACTIVE_STATUS_CHOICES,
        widget=RadioSelect,
        label="Active Status"
    )
    
    is_staff = forms.ChoiceField(
        choices=STAFF_STATUS_CHOICES,
        widget=RadioSelect,
        label="Staff Status"
    )
    
    is_superuser = forms.ChoiceField(
        choices=SUPERUSER_STATUS_CHOICES,
        widget=RadioSelect,
        label="Super User Status"
    )

    def __init__(self, *args, **kwargs):
        # Check if the form is being initialized for editing
        user_instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        
        if user_instance:
            # If editing a user, make password field optional
            self.fields['password'] = forms.CharField(
                label="Password",
                widget=forms.PasswordInput,
                required=False  # Password is not required when editing
            )
        
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("username", label="Username"),
            Field("first_name", label="First Name"),
            Field("last_name", label="Last Name"),
            Field("email", label="Email Address"),
            Field("password", label="Password"),  # Optional now
            Field("password2"),  
            Field("is_active"),  
            Field("is_staff"), 
            Field("is_superuser"), 
            Submit("Create User", "Submit", css_class="btn btn-success"),
        )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "is_active", "is_staff", "email", "is_superuser"]
        widgets = {
            "password": forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
