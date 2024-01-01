from django import forms
from .models import Order

class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_First_Name', 'order_Last_Name', 'order_company_type']
        exclude = ['owner']

    