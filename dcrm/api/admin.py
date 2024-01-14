from django.contrib import admin
from .models import Order, Company, Comment

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
       list_display = ['status', 'order_Number','company', 'order_First_Name', 'order_Last_Name', 'order_Mobile', 'order_Created']

@admin.register(Company)
class OrderAdmin(admin.ModelAdmin):
       list_display = ['company_Type','company_Name', 'company_Employees']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
       list_display = ['owner', 'order', 'created', 'body'] 
       list_filter = ['owner', 'created', 'order']
       search_fields = ['owner', 'order', 'body']


