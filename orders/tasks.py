from celery import task

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

from io import BytesIO

import weasyprint

from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'Your order was successfully created.\n' \
              f'Your order ID is {order.id}.'

    email = EmailMessage(
        subject,
        message,
        'admin@my_shop.store',
        [order.email]
    )

    # generate pdf
    html = render_to_string('orders/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = []
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/style.css')])
    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    email.send()


@task
def status_change_notification(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f"Status of your order ID {order.id} was changed to '{order.status}'"

    mail_sent = send_mail(
        subject,
        message,
        'admin@my_shop.store',
        [order.email]
    )

    return mail_sent


@task
def payment_status(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'your order ID {order.id} has been paid'

    mail_sent = send_mail(
        subject,
        message,
        'admin@my_shop.store',
        [order.email]
    )

    return mail_sent
