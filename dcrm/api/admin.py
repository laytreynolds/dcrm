from django.contrib import admin
from .models import Order, Company

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
       list_display = ['order_Open','status', 'order_Number', 'order_First_Name', 'order_Last_Name', 'order_Mobile', 'order_Created']

@admin.register(Company)
class OrderAdmin(admin.ModelAdmin):
       list_display = ['company_Type','company_Name', 'company_Employees']


