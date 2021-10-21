from django.contrib import admin

from .models import Order, OrderItems
from .tasks import status_change_notification


def status_change(queryset, status):
    for order in queryset:
        order.status = status
        order.save()

        status_change_notification.delay(order.id)


def status_created(modeladmin, request, queryset):
    status_change(queryset, 'Created')


def status_processing(modeladmin, request, queryset):
    status_change(queryset, 'Processing')


def status_ready_for_pickup(modeladmin, request, queryset):
    status_change(queryset, 'Ready for pickup')


def status_shipped(modeladmin, request, queryset):
    status_change(queryset, 'Shipped')


def status_completed(modeladmin, request, queryset):
    status_change(queryset, 'Completed')


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

    actions = [status_created, status_processing, status_ready_for_pickup, status_shipped, status_completed]
