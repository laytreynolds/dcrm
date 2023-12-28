from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order


# Create your views here.
def Main(request):
    return render(request, "base.html")

def Connected(request):
    connected = Order.objects.filter(status=Order.Status.connected)
    return render(request, "connected.html", {"connected": connected})


def Orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})


def OrderDetail(request, order_Id):
    try:
        order = Order.objects.get(order_Id=order_Id)
    except Order.DoesNotExist:
        raise Http404("No Post found.")
    return render(request, "order_detail.html", {"order": order})
