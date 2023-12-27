from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Company, User, Order


# Create your views here.
def connect_list(request):
    orders = Order.connected.all()
    return render(request, "api/orders/list.html", {"orders": orders})


def connect_detail(request, id):
    order = get_object_or_404(Order, id=id, status=Order.Status.connected)
    return render(request, "api/order/detail.html", {"order": order})
