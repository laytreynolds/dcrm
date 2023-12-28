from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order


# Create your views here.
def Home(request):
    return render(request, "base.html")


def Connected(request):
    connected = Order.objects.filter(status=Order.Status.connected)
    return render(request, "order/connected.html", {"connected": connected})


def Orders(request):
    orders = Order.objects.all()
    return render(request, "order/orders.html", {"orders": orders})


def OrderDetail(request, order_Id):
    try:
        order = Order.objects.get(order_Id=order_Id)
    except Order.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "order/detail.html", {"order": order})
