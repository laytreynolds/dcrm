from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path("", views.Home, name='home'),
    path('orders/', views.Orders, name='orders'),
    path('order/<int:order_Id>', views.OrderDetail, name='OrderDetail'),


]