from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Order, Comment
from django.views.generic import ListView, DetailView, View
from .forms import SearchForm, OrderForm, CommentForm
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.utils.timezone import now




# Globals

pagination = 10

# HOME


@login_required
def Home(request):
    return render(request, "home.html")


# ORDER


class OrderSearch(LoginRequiredMixin, ListView):
    def get(self, request):
        form = SearchForm()
        query = None
        results = []

        if "query" in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data["query"]
                vector = SearchVector(
                    "order_Email",
                    "order_company_name",
                    "order_Number",
                    "order_Mobile",
                    "order_First_Name",
                    "order_Last_Name",
                )
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
    paginate_by = pagination
    template_name = "order/orders_list.html"


class OrdersTodayListView(LoginRequiredMixin, ListView):
    queryset = Order.today.all()
    context_object_name = "OrdersToday"
    paginate_by = pagination
    template_name = "order/today.html"


class OrdersThisMonthView(LoginRequiredMixin, ListView):
    queryset = Order.month.all()
    context_object_name = "OrdersThisMonth"
    paginate_by = pagination
    template_name = "order/month.html"


class OrdersThisweekView(LoginRequiredMixin, ListView):
    queryset = Order.week.all()
    context_object_name = "OrdersThisWeek"
    paginate_by = pagination
    template_name = "order/week.html"

class ConnectionsThisMonth(LoginRequiredMixin, ListView):
    queryset = Order.connected.filter(order_Created__month=now().month)
    context_object_name = "ConnectionsThisMonth"
    paginate_by = pagination
    template_name = "order/connected_month.html"


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "order/detail.html"
    context_object_name = "OrderDetail"
    slug_field = "order_Id"
    slug_url_kwarg = "order_Id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['form'] = CommentForm()
        context['comments'] = order.comments.all()
        return context



class NewOrder(LoginRequiredMixin, View):
    model = Order
    method = ["get", "post"]

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
            return redirect("crm:OrderDetailView", order_Id=order.order_Id)
        return render(request, "order/new.html", {"form": form})


class OrderUpdate(LoginRequiredMixin, View):
    model = Order

    def get(self, request, order_Id):
        order = Order.objects.get(order_Id=order_Id)
        form = OrderForm(instance=order)
        return render(request, "order/update.html", {"form": form, "order": order})

    def post(self, request, order_Id):
        order = Order.objects.get(order_Id=order_Id)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            form.save()
            return redirect("crm:OrderDetailView", order_Id=order_Id)
        return render(request, "order/update.html", {"form": form, "order": order})


# COMPANY


def NewCompany(request):
    return render(request, "company/new.html")


# Comment


class OrderComment(LoginRequiredMixin, View):

    def get(self, request, order_Id):
        order = Order.objects.get(order_Id=order_Id)
        form = OrderForm(order_id=order_Id)
        return render(request, "order/comment_form.html", {"form": form, "order": order})

    def post(self, request, order_Id):
        order = get_object_or_404(Order, order_Id=order_Id)
        comment = None
        # A comment was posted
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a Comment object without saving it to the database 
                comment = form.save(commit=False)
            # Assign the order to the comment
                comment.order = order
                comment.owner = request.user
            # Save the comment to the database
                comment.save()
        return redirect("crm:OrderDetailView", order_Id=order.order_Id)



class Dashboard(LoginRequiredMixin, View):
    template_name = "order/home.html"

    def get(self, request):

        # Calculate total box value using the model manager

        # Daily values 
        revenue_today = Order.today.aggregate(total=Sum("order_box_value"))["total"]
        revenue_week = Order.week.aggregate(total=Sum("order_box_value"))["total"]
        revenue_month = Order.month.aggregate(total=Sum("order_box_value"))["total"]

        # Connected values
        connected_revenue_month = Order.connected.filter(order_Created__month=now().month).aggregate(total=Sum("order_box_value"))["total"]
        monthly_users_leaderboard = User.objects.annotate(total_box_value=Sum('sales__order_box_value')).order_by('-total_box_value')[:10]
        


        # Agent Values


        # Include the total_box_value in the context
        context = {"revenue_today": revenue_today, "revenue_month": revenue_month, "revenue_week": revenue_week,"connected_revenue_month": connected_revenue_month, 'monthly_users_leaderboard': monthly_users_leaderboard}
        return render(request, "home.html", context)
