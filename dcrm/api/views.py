from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order
from django.utils.timezone import now
from datetime import date




# ORDER

def Home(request):
    return render(request, "base.html")

def TodayOrders(request):
    #current_date = now().date()
    orders = Order.today.all()
    return render(request, "order/today.html", {'orders': orders})

def ThisMonthOrders(request):
    orders = Order.month.all()
    return render(request, "order/month.html", {'orders': orders})


def Orders(request):
    orders = Order.objects.all()
    return render(request, "order/orders.html", {"orders": orders})


def OrderDetail(request, order_Id):
    try:
        order = Order.objects.get(order_Id=order_Id)
    except Order.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "order/detail.html", {"order": order})

def NewOrder(request):
    return render(request, "order/new.html")


# COMPANY

def NewCompany(request):
    return render(request, "company/new.html")