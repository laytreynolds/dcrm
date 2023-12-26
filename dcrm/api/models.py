from django.db import models
import string, random


def generate_order_number():
    while True:
        order_number = ''.join(random.choices(string.ascii_lowercase, k=6))
        # Check if the generated order number already exists
        if Order.objects.filter(order_number=order_number).count() == 0:
            break
    return order_number

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default="No Email")
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(unique=True, max_length=6, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_created_at = models.DateTimeField(auto_now_add=True)