from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path("", views.Main, name='home'),
    path('orders/', views.Orders, name='orders'),
    path('order/<int:order_Id>', views.OrderDetail, name='order_Detail'),


]