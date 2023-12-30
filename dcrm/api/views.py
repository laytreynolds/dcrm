from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Company, User, Order
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector

# HOME 

def Home(request):
    return render(request, "base.html")

# AUTHENTICATION

def LoginUser(request):
    pass

def LogoutUser(request):
    pass


# ORDER

def OrderSearch(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            vector = SearchVector('order_Number')  # Specify the fields to search
            results = Order.objects.annotate(search=vector).filter(search=query)

    return render(request, 'order/search.html', {'form': form, 'query': query, 'results': results})


class OrdersListView(ListView):
    queryset = Order.objects.all()
    context_object_name = 'Orders'
    paginate_by = 3
    template_name = "order/orders_list.html"


class OrdersTodayListView(ListView):
    queryset = Order.today.all()
    context_object_name = 'OrdersToday'
    paginate_by = 3
    template_name = "order/today.html"


class OrdersThisMonthView(ListView):
    queryset = Order.month.all()
    context_object_name = 'OrdersThisMonth'
    paginate_by = 3
    template_name = 'order/month.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'OrderDetail'
    slug_field = 'order_Number'
    slug_url_kwarg = 'order_Number'

def NewOrder(request):
    return render(request, "order/new.html")


# COMPANY

def NewCompany(request):
    return render(request, "company/new.html")