from django.db import models
import string, random
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.postgres.search import SearchVectorField



# Generate randomm unique CRM-xxxxxx Number


def generate_order_number():
    while True:
        order_Number = "CRM-" + "".join(random.choices(string.digits, k=6))
        # Check if the generated order number already exists
        if Order.objects.filter(order_Number=order_Number).count() == 0:
            break
    return order_Number


# COMPANY


class Company(models.Model):
    company_Name = models.CharField(max_length=255, default="")
    id = models.AutoField(primary_key=True)
    compapy_Created = models.DateTimeField(auto_now=True)
    company_Updated = models.DateTimeField(auto_now=True)
    company_Type = models.CharField(max_length=100, default="")
    company_Employees = models.IntegerField(default=0)
    company_Number_Of_Orders = models.IntegerField(default=1)
    company_Monthly_Spend = models.FloatField(default=1)

    class Meta:
        verbose_name_plural = "Companies"
        indexes = [models.Index(fields=["company_Monthly_Spend"])]
        ordering = ["company_Name"]

    def __str__(self):
        return self.company_Name


# ORDER

# MANAGER


class TodayManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(order_Created__date=now().date())

class MonthManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(order_Created__month=now().month)


class Order(models.Model):
    def save(self, *args, **kwargs):
        if not self.order_Number:
            self.order_Number = generate_order_number()
        super(Order, self).save(*args, **kwargs)

    class Status(models.TextChoices):
        new = "NW", "New"
        held = "HD", "Held"
        parked = "PK", "Parked"
        to_Process = "TP", "To Process"
        future_End_Date = "FD", "Future End Date"
        awaiting_Stock = "AW", "Awaiting Stock"
        issues = "IS", "Issues"
        connected = "CN", "Connected"

    order_Id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(
        User, related_name="sales", on_delete=models.PROTECT, default=""
    )
    order_Number = models.CharField(
        unique=True, max_length=255, default="", editable=False
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="orders"
    )
    order_Created = models.DateTimeField(auto_now=True)
    order_Updated = models.DateTimeField(auto_now=True)
    order_Title = models.CharField(max_length=100, default="")
    order_First_Name = models.CharField(max_length=100, default="")
    order_Last_Name = models.CharField(max_length=100, default="")
    order_Mobile = models.CharField(max_length=11, default="")
    order_Landline = models.CharField(max_length=11, default="")
    order_Email = models.EmailField(default="")
    order_House_Number = models.CharField(max_length=100, default="")
    order_Street = models.CharField(max_length=255, default="")
    order_City = models.CharField(max_length=255, default="")
    order_County = models.CharField(max_length=255, default="")
    order_Postcode = models.CharField(max_length=255, default="")
    order_Delivery_House_Number = models.CharField(max_length=255, default="")
    order_Delivery_Street = models.CharField(max_length=255, default="")
    order_Delivery_City = models.CharField(max_length=255, default="")
    order_Delivery_County = models.CharField(max_length=255, default="")
    order_Delivery_Postcode = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.new)

    order_Open = models.BooleanField()

    objects = models.Manager()
    today = TodayManager() 
    month = MonthManager()


    class Meta:
        ordering = ["-order_Created"]
        indexes = [models.Index(fields=["order_Mobile"])]
        default_manager_name = "objects"

    def __str__(self):
        return self.order_Number

    def get_absolute_url(self):
        return reverse("crm:OrderDetailView", args=[self.order_Number])
