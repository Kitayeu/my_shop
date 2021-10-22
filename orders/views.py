from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required

from decimal import Decimal

import weasyprint

from .models import OrderItems, Product, Order
from .forms import OrderCreateForm
from carts.views import get_cart, cart_clear
from .tasks import order_created


def order_create(request):
    cart = get_cart(request)

    cart_qty = sum(item['quantity'] for item in cart.values())
    transport_cost = round((22 + cart_qty // 10), 2)

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']
            if transport == 'Recipient pickup':
                transport_cost = 0

            order = order_form.save(commit=False)

            if request.user.is_authenticated:
                order.user = request.user

            order.transport_cost = Decimal(transport_cost)
            order.save()

            product_ids = cart.keys()
            products = Product.objects.filter(id__in=product_ids)

            for product in products:
                cart_item = cart[str(product.id)]
                OrderItems.objects.create(
                    order=order,
                    product=product,
                    price=cart_item['price'],
                    quantity=cart_item['quantity']
                )
                cart_clear(request)  # cleaning cart

                order_created.delay(order.id)  # starting an asynchronous task

                return render(request,
                              'orders/order_created.html',
                              {'order': order}
                              )
    else:
        order_form = OrderCreateForm()

        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'telephone': request.user.profile.phone_number,
                'address': request.user.profile.address,
                'postal_code': request.user.profile.postal_code,
                'city': request.user.profile.city,
                'country': request.user.profile.country,
            }
            order_form = OrderCreateForm(initial=initial_data)

    return render(request,
                  'orders/order_create.html',
                  {'cart': cart,
                   'order_form': order_form,
                   'transport_cost': transport_cost}
                  )


@staff_member_required
def invoice_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'

    # generate pdf
    html = render_to_string('orders/pdf.html', {'order': order})
    stylesheets = []
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/style.css')])
    return response
