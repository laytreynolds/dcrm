from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order
from django.core.paginator import Paginator




# ORDER

def Home(request):
    return render(request, "base.html")

def TodayOrders(request):
    order_list = Order.today.all()
    paginator = Paginator(order_list, 2) 
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
    except:
        orders = paginator.page(paginator.num_pages)
    return render(request, "order/today.html", {'orders': orders})


def ThisMonthOrders(request):
    order_list = Order.month.all()
    paginator = Paginator(order_list, 2) 
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
    except:
        orders = paginator.page(paginator.num_pages)
    return render(request, "order/month.html", {'orders': orders})


def Orders(request):
    orders = Order.objects.all()
    return render(request, "order/orders.html", {"orders": orders})


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