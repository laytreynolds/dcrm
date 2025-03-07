from django.db.models import Sum, Value, IntegerField, FloatField, Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Order, Campaign, Activity, Comment
from django.views.generic import ListView, DetailView, View
from .forms import SearchForm, OrderForm, CommentForm, OrderUpdateForm, CreateUserForm
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.utils.timezone import now
from django.db.models.functions import Coalesce
from django.contrib import messages
from datetime import datetime, timedelta
from django.views.generic import DeleteView
from django.urls import reverse_lazy
import csv
from django.http import HttpResponse
from django.utils import timezone
from .mixins import OrderFilterMixin


# Globals

pagination = 9

# HOME


@login_required
def Home(request):
    return render(request, "home.html")


# ACTIVITY


class OrderActivity(LoginRequiredMixin, View):
    pass


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


class OrdersListView(LoginRequiredMixin, OrderFilterMixin, ListView):
    model = Order
    template_name = 'order/orders_list.html'
    context_object_name = 'Orders'
    paginate_by = 9

    def get_queryset(self):
        # This will first get all orders, then apply filters if any
        return super().get_queryset()


class OrdersTodayListView(LoginRequiredMixin, ListView):
    queryset = Order.today.all()
    context_object_name = "OrdersToday"
    paginate_by = pagination
    template_name = "order/today.html"


class OrdersThisMonth(LoginRequiredMixin, OrderFilterMixin, ListView):
    model = Order
    template_name = 'order/month.html'
    context_object_name = 'OrdersThisMonth'
    paginate_by = 9

    def get_queryset(self):
        # First get this month's orders
        today = timezone.now()
        first_day = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        queryset = Order.objects.filter(order_Created__gte=first_day)
        # Then apply any additional filters
        return super().get_queryset().filter(order_Created__gte=first_day)


class OrdersThisweek(LoginRequiredMixin, OrderFilterMixin, ListView):
    model = Order
    template_name = 'order/week.html'
    context_object_name = 'OrdersThisWeek'
    paginate_by = 9

    def get_queryset(self):
        # First get the base queryset from parent
        queryset = super().get_queryset()
        # Get the start of the current week (Monday)
        today = timezone.now()
        start_of_week = today - timedelta(days=today.weekday())
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Add some debug logging or print statements
        filtered_queryset = queryset.filter(order_Created__gte=start_of_week)
                
        return filtered_queryset



class ConnectionsThisMonth(LoginRequiredMixin, OrderFilterMixin, ListView):
    queryset = Order.connected.filter(order_connected_date__month=now().month)
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
        obj = self.get_object()

        # Retrieve all history records and order them by date
        history_records = list(obj.history.all().order_by("-history_date"))

        # Prepare a list to hold changes
        changes_list = []
        
        if len(history_records) >= 2:
            current_record = history_records[0]  # Latest record
            
            for previous_record in history_records[1:]:
                delta = current_record.diff_against(previous_record)
                
                for field in delta.changed_fields:
                    old_value = getattr(previous_record, field)
                    new_value = getattr(current_record, field)

                    # Check if the field is the status field
                    if field == 'status':
                        old_value = Order.Status(old_value).label  # Get full name for old value
                        new_value = Order.Status(new_value).label  # Get full name for new value
                    
                    if field == 'order_company_type':
                        old_value = Order.CompanyType(old_value).label  # Get full name for old value
                        new_value = Order.CompanyType(new_value).label  # Get full name for new value
                    
                    if field == 'order_Title':
                        old_value = Order.Title(old_value).label  # Get full name for old value
                        new_value = Order.Title(new_value).label  # Get full name for new value

                    # Use the history date from the current record as the change date
                    change_date = current_record.history_date if hasattr(current_record, 'history_date') else datetime.now()

                    changes_list.append({
                        'field': field,
                        'old': old_value,
                        'new': new_value,
                        'date': change_date,
                        'user': previous_record.history_user,
                    })
                    
                current_record = previous_record  # Update for the next comparison

        context["history_records"] = history_records
        context["changes_list"] = changes_list  # List of changes for display
        context["form"] = CommentForm()
        context["comments"] = obj.comments.all()
        
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
            messages.success(request, "Order created successfully")
            return redirect("crm:OrderDetailView", order_Id=order.order_Id)
        else:
            messages.error(request, 'Error Creating order')
        return render(request, "order/new.html", {"form": form})


class OrderUpdate(LoginRequiredMixin, View):
    model = Order

    def get(self, request, order_Id):
        order = Order.objects.get(order_Id=order_Id)
        form = OrderUpdateForm(instance=order)
        return render(request, "order/update.html", {"form": form, "order": order})

    def post(self, request, order_Id):
        order = Order.objects.get(order_Id=order_Id)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            form.save()
            messages.success(request, "Order updated successfully")
            return redirect("crm:OrderDetailView", order_Id=order_Id)
        else:
            messages.error(request, 'Error updating order')
        return render(request, "order/update.html", {"form": form, "order": order})


# COMPANY


def NewCompany(request):
    return render(request, "company/new.html")


# Comment


class OrderComment(LoginRequiredMixin, View):

    def post(self, request, order_Id):
        order = get_object_or_404(Order, order_Id=order_Id)
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
    
    
class OrderCommentUpdate(LoginRequiredMixin, View):
    model = Comment

    def post(self, request, order_Id):
        order = get_object_or_404(Order, order_Id=order_Id)
        
        # Get the comment ID and status from the request
        comment_id = request.POST.get('comment_id')
        status = request.POST.get('status')  # Ensure this is included in your form

        # Get the specific comment to update
        comment = get_object_or_404(Comment, id=comment_id)

        # Update the comment's status
        comment.status = status
        comment.save()

        # Redirect to the order detail view
        return redirect("crm:OrderDetailView", order_Id=order.order_Id)

# DASHBOARD

class Dashboard(LoginRequiredMixin, View):
    template_name = "order/home.html"

    def get(self, request):
        # Calculate total box value using the model manager

        # Daily values
        revenue_today = Order.today.aggregate(total=Sum("order_box_value"))["total"]
        revenue_week = Order.week.aggregate(total=Sum("order_box_value"))["total"]
        revenue_month = Order.month.aggregate(total=Sum("order_box_value"))["total"]

        # Connected values
        connected_revenue_month = Order.connected.filter(
            order_Created__month=now().month
        ).aggregate(total=Sum("order_box_value"))["total"]

        monthly_users_leaderboard = User.objects.annotate(
            total_box_value=Sum("sales__order_box_value")
        ).order_by("total_box_value")[:10]

        monthly_users_leaderboard = (
            User.objects.filter(sales__isnull=False)
            .annotate(
                total_box_value=Coalesce(
                    Sum("sales__order_box_value", output_field=FloatField()),
                    Value(0.00),
                )
            )
            .order_by("-total_box_value")[:10]
        )

        # Campaigns

        campaign = (
            Campaign.objects.filter(sales__isnull=False)
            .annotate(
                total_campaign_value=Coalesce(
                    Sum("sales__order_box_value", output_field=FloatField()),
                    Value(0.00),
                )
            )
            .order_by("-total_campaign_value")
        )

        # Include the total_box_value in the context
        context = {
            "campaign": campaign,
            "revenue_today": revenue_today,
            "revenue_month": revenue_month,
            "revenue_week": revenue_week,
            "connected_revenue_month": connected_revenue_month,
            "monthly_users_leaderboard": monthly_users_leaderboard,
        }
        return render(request, "home.html", context)

class Admin(LoginRequiredMixin, ListView):
    context_object_name = "Users"
    paginate_by = pagination
    template_name = "admin/admin.html"

    def get_queryset(self):
        # Order users by last_login field
        return User.objects.all().order_by('last_login')
    
class CreateUser(LoginRequiredMixin, View):
    
    model = User
    method = ["get", "post"]
    
    def get(self, request):
        form = CreateUserForm
        return render(request, "admin/createuser.html", { "form": form})
    
    def post(self, request):
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect("crm:Admin")
        else:
            # If the form is not valid, render the form again with errors
            return render(request, "admin/createuser.html", {"form": user_form})

class EditUser(LoginRequiredMixin, View):
    
    def get(self, request, id):
        user = User.objects.get(id=id)
        form = CreateUserForm(instance=user)
        return render(request, "admin/edituser.html", {"form": form, "user": user})
    
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = CreateUserForm(request.POST, instance=user)

        if form.is_valid():
            # Save the changes to the user
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])  # Set password if changed
            new_user.save()
            return redirect("crm:Admin")  # Redirect after successful update

        return render(request, "admin/edituser.html", {"form": form, "user": user})  # Re-render with errors
    
class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'admin/deleteuser.html'  # Template to confirm deletion
    success_url = reverse_lazy('crm:Admin')  # Redirect after deletion

    def get_queryset(self):
        return User.objects.all()
        # Example: prevent superuser deletion  # Get all users for deletion

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_superuser:
            messages.warning(request, "You cannot delete a superuser.")
            return redirect(self.success_url)
        else:
            messages.success(request, "User Deleted")
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Check if there are any users before rendering the delete confirmation
        if not User.objects.exists():
            messages.warning(request, "No users available to delete.")
            return redirect(self.success_url)
        
        return super().get(request, *args, **kwargs)


class MyOrders(LoginRequiredMixin, OrderFilterMixin, ListView):
    model = Order
    template_name = 'order/myorders.html'
    context_object_name = 'MyOrders'
    paginate_by = 9

    def get_queryset(self):
        # First get user's orders
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset

class ExportMonthCSV(LoginRequiredMixin, View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="connections-month_{datetime.now().strftime("%Y%m")}.csv"'
        
        writer = csv.writer(response)
        writer.writerow([
            'Order Number',
            'Business',
            'Contact',
            'Box Value',
            'Campaign',
            'Owner',
            'Mobile',
            'Connection Type',
            'Created',
            'Status'
        ])
        
        # Get the same queryset as connected_month view
        orders = Order.connected.filter(order_connected_date__month=now().month)
        
        for order in orders:
            writer.writerow([
                order.order_Number,
                order.order_company_name,
                f"{order.order_First_Name} {order.order_Last_Name}",
                order.order_box_value,
                order.campaign,
                order.owner,
                order.order_Mobile,
                order.order_connection_type,
                order.order_Created,
                order.get_status_display()
            ])
        
        return response

