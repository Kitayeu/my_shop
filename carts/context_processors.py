from decimal import Decimal

from .views import get_cart


def cart(request):
    cart = get_cart(request)
    cart_total_price = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())
    return {'cart_total_price': cart_total_price}
