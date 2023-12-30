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


def ThisMonthOrders(request):
    order_list = Order.month.all()
    paginator = Paginator(order_list, 10) 
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, "order/month.html", {'orders': orders})

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