from django.db import models
import string, random


def generate_order_number():
    while True:
        order_number = "CRM-".join(random.choices(string.ascii_lowercase, k=6))
        # Check if the generated order number already exists
        if Order.objects.filter(order_number=order_number).count() == 0:
            break
    return order_number


# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    compapy_created = models.DateTimeField(auto_now=True)
    company_updated = models.DateTimeField(auto_now=True)
    company_type = models.CharField(max_length=100, default='')
    company_employees = models.IntegerField(default=0)
    company_number_of_orders = models.IntegerField(default=1)
    company_monthly_spend = models.FloatField(default=1)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(unique=True, max_length=15, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    order_created = models.DateTimeField(auto_now=True)
    order_updated = models.DateTimeField(auto_now=True)
    order_title = models.CharField(max_length=100,default='')
    order_first_name = models.CharField(max_length=100,default='')
    order_last_name = models.CharField(max_length=100,default='')
    order_mobile = models.CharField(max_length=11,default='')
    order_landline = models.CharField(max_length=11,default='')
    order_email = models.EmailField(default='')
    order_house_number = models.CharField(max_length=100,default='')
    order_street = models.CharField(max_length=255,default='')
    order_city = models.CharField(max_length=255,default='')
    order_county = models.CharField(max_length=255,default='')
    order_post_code = models.CharField(max_length=255,default='')
    order_delivery_house_number = models.CharField(max_length=255,default='')
    order_delivery_street = models.CharField(max_length=255,default='')
    order_delivery_city = models.CharField(max_length=255,default='')
    order_delivery_county = models.CharField(max_length=255,default='')
    order_delivery_post_code = models.CharField(max_length=255,default='')

    class Meta:
        ordering = ['-order_created']


def save(self, *args, **kwargs):
    if not self.order_number:
        self.order_number = generate_order_number()
    super(Order, self).save(*args, **kwargs)


def __str__(self):
    return self.title
