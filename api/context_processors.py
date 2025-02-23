from .models import Order

def order_context(request):
    return {
        'Order': Order
    } 