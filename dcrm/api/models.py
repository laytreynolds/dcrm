from django.db import models
import string, random
from django.contrib.auth.models import User


def generate_order_number():
    while True:
        order_Number = "CRM-".join(random.choices(string.ascii_lowercase, k=6))
        # Check if the generated order number already exists
        if Order.objects.filter(order_number=order_Number).count() == 0:
            break
    return order_Number


# Create your models here.
class Company(models.Model):
    company_Name = models.CharField(max_length=255, default='')
    id = models.AutoField(primary_key=True)
    compapy_Created = models.DateTimeField(auto_now=True)
    company_Updated = models.DateTimeField(auto_now=True)
    company_Type = models.CharField(max_length=100, default='')
    company_Employees = models.IntegerField(default=0)
    company_Number_of_orders = models.IntegerField(default=1)
    company_Monthly_spend = models.FloatField(default=1)


class Order(models.Model):

    class Status(models.TextChoices):
        new = 'NW', 'New'
        held = 'HD', 'Held'
        parked = 'PK', 'Parked'
        to_Process = 'TP', 'To Process'
        future_End_Date = 'FD', 'Future End Date'
        awaiting_Stock = 'AW', 'Awaiting Stock'
        issues = 'IS', 'Issues'
        connected = 'CN','Connected'

    order_Id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User,
                              related_name='sales',
                              on_delete=models.PROTECT,
                              default='')
    order_Number = models.CharField(unique=True, max_length=15, editable=False)
    company = models.ForeignKey(Company, 
                                on_delete=models.CASCADE,
                                related_name='orders')
    order_Created = models.DateTimeField(auto_now=True)
    order_Updated = models.DateTimeField(auto_now=True)
    order_Title = models.CharField(max_length=100,default='')
    order_First_name = models.CharField(max_length=100,default='')
    order_Last_name = models.CharField(max_length=100,default='')
    order_Mobile = models.CharField(max_length=11,default='')
    order_Landline = models.CharField(max_length=11,default='')
    order_Email = models.EmailField(default='')
    order_House_number = models.CharField(max_length=100,default='')
    order_Street = models.CharField(max_length=255,default='')
    order_City = models.CharField(max_length=255,default='')
    order_County = models.CharField(max_length=255,default='')
    order_Post_code = models.CharField(max_length=255,default='')
    order_Delivery_house_number = models.CharField(max_length=255,default='')
    order_Delivery_street = models.CharField(max_length=255,default='')
    order_Delivery_city = models.CharField(max_length=255,default='')
    order_Delivery_county = models.CharField(max_length=255,default='')
    order_Delivery_post_code = models.CharField(max_length=255,default='')
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.new)



    class Meta:
        ordering = ['-order_Created']
        indexes = [
            models.Index(fields=['order_Created'])
        ]

def save(self, *args, **kwargs):
    if not self.order_Number:
        self.order_Number = generate_order_number()
    super(Order, self).save(*args, **kwargs)


def __str__(self):
    return self.title
