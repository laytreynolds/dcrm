from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'crm'

urlpatterns = [
    path("", views.Dashboard.as_view(), name='dashboard'),
    path('orders/', views.OrdersListView.as_view(), name='OrdersListView'),
    path('<int:order_Id>', views.OrderDetailView.as_view(), name='OrderDetailView'),
    path("new/order", views.NewOrder.as_view(), name='NewOrder'),
    path("new/company", views.NewCompany, name='NewCompany'),
    path("orders/today", views.OrdersTodayListView.as_view(), name='OrdersToday'),
    path("orders/month", views.OrdersThisMonthView.as_view(), name='OrderThisMonth'),
    path("orders/connected/month", views.ConnectionsThisMonth.as_view(), name='ConnectionsThisMonth'),
    path('search/', views.OrderSearch.as_view(), name='OrderSearch'),
    path('orders/week', views.OrdersThisweekView.as_view(), name='OrdersThisWeek'),
    path('update/<int:order_Id>/', views.OrderUpdate.as_view(), name='OrderUpdate'),
    path('comment/<int:order_Id>/',views.OrderComment.as_view(), name='OrderComment'),
    path('comment/update/<int:order_Id>/',views.OrderCommentUpdate.as_view(), name='OrderCommentUpdate'),
    path('admin', views.Admin.as_view(), name='Admin'),
    path("admin/createuser", views.CreateUser.as_view(), name='CreateUser'),
    path("admin/deleteuser/<int:pk>/", views.DeleteUser.as_view(), name='DeleteUser'),
    path('admin/updateuser/<int:id>', views.EditUser.as_view(), name='EditUser'),
    path('my/orders', views.MyOrders.as_view(), name='MyOrders'),
]