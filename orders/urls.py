from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/pdf/', views.invoice_pdf, name='invoice_pdf'),
    path('order/<int:order_id>/pdf/', views.invoice_pdf, name='customer_invoice_pdf'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
