from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView

# HOME 

def Home(request):
    return render(request, "base.html")

# AUTHENTICATION

def LoginUser(request):
    pass

def LogoutUser(request):
    pass


# ORDER

class OrdersListView(ListView):
    queryset = Order.objects.all()
    context_object_name = 'Orders'
    paginate_by = 10
    template_name = "order/orders_list.html"


class OrdersTodayListView(ListView):
    queryset = Order.today.all()
    context_object_name = 'OrdersToday'
    paginate_by = 10
    template_name = "order/today.html"


class OrdersThisMonthView(ListView):
    queryset = Order.month.all()
    template_name = 'order/month.html'
    context_object_name = 'OrdersThisMonth'
    paginate_by = 10


def OrderDetail(request, order_Number):
    try:
        order = Order.objects.get(order_Number=order_Number)
    except Order.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "order/detail.html", {"order": order})

def NewOrder(request):
    return render(request, "order/new.html")


# COMPANY

def NewCompany(request):
    return render(request, "company/new.html")