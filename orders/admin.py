from django.contrib import admin

from .models import Order, OrderItems


class OrderItemInline(admin.TabularInline):
    model = OrderItems


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email',
        'address', 'postal_code', 'city', 'paid',
        'transport', 'created', 'status',
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
