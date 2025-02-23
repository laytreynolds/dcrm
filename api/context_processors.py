from .models import Order, User

def order_context(request):
    return {
        'Order': Order,
        'Users': User
    } 