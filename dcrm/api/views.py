from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order


# Create your views here.
def connected(request):
    connected = Order.objects.filter(status=Order.Status.connected)
    return render(request, "connected.html", {"connected": connected})

def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})
