from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'crm'

urlpatterns = [
    path("", views.Home, name='home'),
    path('orders/', views.OrdersListView.as_view(), name='OrdersListView'),
    path('<str:order_Number>', views.OrderDetailView.as_view(), name='OrderDetailView'),
    path("new/order", views.NewOrder.as_view(), name='NewOrder'),
    path("new/company", views.NewCompany, name='NewCompany'),
    path("orders/today", views.OrdersTodayListView.as_view(), name='OrdersToday'),
    path("orders/month", views.OrdersThisMonthView.as_view(), name='OrderThisMonth'),
    path('search/', views.OrderSearch.as_view(), name='OrderSearch'),
]