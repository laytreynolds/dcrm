from django.db import models
import string, random
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
import datetime


# Generate randomm unique CRM-xxxxxx Number


def generate_order_number():
    while True:
        order_Number = "".join(random.choices(string.digits, k=6))
        # Check if the generated order number already exists
        if Order.objects.filter(order_Number=order_Number).count() == 0:
            break
    return order_Number


class Campaign(models.Model):

    name = models.CharField(default="", null=True)
    target = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"



# Activity
    
class Activity(models.Model):
    text = models.TextField(default=None, null=True, blank=True)
    changed_date = models.DateField(auto_now_add=True)
    changed_by = models.ForeignKey(User, related_name="user", on_delete=models.PROTECT)
    

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

class ConnectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="CN")


class TodayManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(order_Created__date=now().date())


class MonthManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(order_Created__month=now().month)


class Weekmanager(models.Manager):
    def get_queryset(self):
        current_week = now().isocalendar()[1]
        return super().get_queryset().filter(order_Created__week=current_week)

class Order(models.Model):
    def save(self, *args, **kwargs):
        if not self.order_Number:
            self.order_Number = generate_order_number()
        if not self.status:
            self.status = "NW"
        if not self.order_Created:
            self.order_Created = datetime.now()
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
        cancelled = "CNL", "Cancelled"

    class CompanyType(models.TextChoices):
        sole_trader = "SOT", "Sole Trader"
        limited_company = "LTD", "Limited Company"
        limited_partnership = "LTP", "Limited Partnership"
        partnership = "PAR", "Partnership"
        limited_liability_parntership = "LLP", "Limited liability Partnership"
        charity = "CHA", "Charity"

    class Title(models.TextChoices):
        Mr = "mr", "Mr"
        Mrs = "mrs", "Mrs"
        Ms = "ms", "Ms"
        Miss = "miss", "Miss"
        Dr = "dr", "Dr"
        Prof = "prof", "Professor"
        Sir = "sir", "Sir"
        Madam = "madam", "Madam"
        Rev = "rev", "Reverend"

    class SIM(models.TextChoices):
        Yes = "Y", "Yes"
        No = "N", "No"

    class Network(models.TextChoices):
        O2 = "O2", "O2"
        EE = "EE", "EE"
        THREE = "THREE", "Three"

    history = HistoricalRecords()
    order_Id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name="sales", on_delete=models.PROTECT, null=True)
    order_Number = models.CharField(unique=True, max_length=255, default="", editable=False)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name="orders")
    order_Created = models.DateTimeField(editable=False)
    order_Updated = models.DateTimeField(auto_now=True)
    order_Title = models.CharField(max_length=20, choices=Title.choices, default="", null=True)
    order_First_Name = models.CharField(max_length=100, default="", null=True)
    order_Last_Name = models.CharField(max_length=100, default="", null=True)
    order_Mobile = models.CharField(max_length=11, default="", null=True)
    order_Landline = models.CharField(max_length=11, default="", null=True, blank=True)
    order_Email = models.EmailField(default="", null=True)
    order_House_Number = models.CharField(max_length=100, default="", null=True, blank=True)
    order_Street = models.CharField(max_length=255, default="", null=True, blank=True)
    order_City = models.CharField(max_length=255, default="", null=True, blank=True)
    order_County = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Postcode = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Delivery_House_Number = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Delivery_Street = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Delivery_City = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Delivery_County = models.CharField(max_length=255, default="", null=True, blank=True)
    order_Delivery_Postcode = models.CharField(max_length=255, default="", null=True, blank=True)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.new)
    order_network = models.CharField(max_length=100, default="", null=True, blank=True)
    order_box_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_deal_source = models.CharField(max_length=255, default="", null=True, blank=True)
    order_connected_date = models.DateField(default="1970-01-01", null=True, blank=True)
    order_loss_reason = models.CharField(max_length=255, default="", null=True, blank=True)
    order_date_of_birth = models.DateField(default="1970-01-01", null=True, blank=True)
    order_account_address = models.TextField(default="", null=True, blank=True)
    campaign = models.ForeignKey(Campaign,related_name="sales", on_delete=models.PROTECT, null=True)
    order_network = models.CharField(choices=Network.choices, default="", null=True)
    order_connection_type = models.CharField(max_length=255, default="", null=True)
    order_eligibility_date = models.DateField(default="1970-01-01", null=True, blank=True)
    order_handset = models.CharField(max_length=255, default="", null=True, blank=True)
    order_tariff = models.CharField(max_length=255, default="", null=True, blank=True)
    order_sim_required = models.CharField(max_length=255, choices=SIM.choices, null=True, default=SIM.Yes)
    order_tariff_code = models.CharField(max_length=255, default="", null=True, blank=True)
    order_spend_cap = models.DecimalField(default=0, decimal_places=2, max_digits=10, null=True)
    order_network_account_number = models.CharField(max_length=255, default="", null=True, blank=True)
    order_additional_details = models.TextField(default="", null=True, blank=True)
    order_commission_details = models.TextField(default="", null=True, blank=True)
    order_Open = models.BooleanField(default=True)
    order_company_type = models.CharField(max_length=20, choices=CompanyType.choices, default="", null=True)
    order_company_name = models.CharField(default="",null=True)

    objects = models.Manager()
    today = TodayManager()
    month = MonthManager()
    week = Weekmanager()
    connected = ConnectManager()

    class Meta:
        ordering = ["-order_Created"]
        indexes = [models.Index(fields=["order_Mobile"])]
        default_manager_name = "objects"

    def __str__(self):
        return f"{self.order_Number} / {self.order_company_name}"

    def get_absolute_url(self):
        return reverse("crm:OrderDetailView", args=[self.order_Id])


# COMMENTS


class Comment(models.Model):
    class Status(models.TextChoices):
        Open = "Open", "Open"
        Closed = "Closed", "Closed"
        InProgress = "In Progress", "In Progress"

    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, default="", null=True)

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["created"]),
        ]

    def __str__(self):
        return f"Comment by {self.owner} on {self.order}"


