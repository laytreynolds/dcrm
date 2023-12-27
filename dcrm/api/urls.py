from django.urls import path
from . import views

urlpatterns = [
    path('connected', views.connect_list, name='connect_list'),
    path('<int:id>', views.connect_detail, name='connect_detail')


]