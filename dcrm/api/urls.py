from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path("", views.Home, name='home'),
    path('orders/', views.Orders, name='Orders'),
    path('order/<int:order_Id>', views.OrderDetail, name='OrderDetail'),
    path("new/order", views.NewOrder, name='NewOrder'),
    path("new/company", views.NewCompany, name='NewCompany'),
    path("orders/today", views.TodayOrders, name='TodayOrders'),




]