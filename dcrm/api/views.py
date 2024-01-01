from django.shortcuts import render, redirect
from .models import Company, User, Order
from django.views.generic import ListView, DetailView, View
from .forms import SearchForm, OrderForm
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user



# HOME


@login_required
def Home(request):
    return render(request, "home.html")


# ORDER


class OrderSearch(ListView):
    def get(self, request):
        form = SearchForm()
        query = None
        results = []

        if "query" in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data["query"]
                vector = SearchVector(
                    "order_Number",
                    "order_Mobile",
                    "order_First_Name",
                    "order_Last_Name",
                    "order_Created",
                )  # Specify the fields to search
                results = Order.objects.annotate(search=vector).filter(
                    Q(search__icontains=query)
                )

        return render(
            request,
            "order/search.html",
            {"form": form, "query": query, "results": results},
        )


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    context_object_name = "Orders"
    paginate_by = 1
    template_name = "order/orders_list.html"


class OrdersTodayListView(LoginRequiredMixin, ListView):
    queryset = Order.today.all()
    context_object_name = "OrdersToday"
    paginate_by = 1
    template_name = "order/today.html"


class OrdersThisMonthView(LoginRequiredMixin, ListView):
    queryset = Order.month.all()
    context_object_name = "OrdersThisMonth"
    paginate_by = 1
    template_name = "order/month.html"


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "order/detail.html"
    context_object_name = "OrderDetail"
    slug_field = "order_Number"
    slug_url_kwarg = "order_Number"


class NewOrder(View):
    model = Order

    def get(self, request):
        form = OrderForm()
        return render(request, "order/new.html", {"form": form})

    def post(self, request):
        current_user = get_user(request)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = current_user
            order.save()
            return redirect("crm:OrderDetailView", order_Number=order.order_Number)
        return render(request, "order/new.html", {"form": form})


# COMPANY


def NewCompany(request):
    return render(request, "company/new.html")
