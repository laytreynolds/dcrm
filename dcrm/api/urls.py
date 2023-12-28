from django.urls import path
from . import views

urlpatterns = [
    path('connected', views.connected, name='connected'),
    path('', views.orders, name='orders')
]