import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Order, OrderItems
from .tasks import status_change_notification, payment_status


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


def export_csv(modeladmin, request, queryset):
    chooses = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={chooses.verbose_name}.csv'
    writer = csv.writer(response)
    fields = [field for field in chooses.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_csv.short_description = 'Export to CSV'


def payment(queryset, paid):
    for order in queryset:
        order.paid = paid
        order.save()

        if paid:
            payment_status.delay(order.id)


def not_paid(modeladmin, request, queryset):
    payment(queryset, False)


not_paid.short_description = 'Not Paid'


def paid_for(modeladmin, request, queryset):
    payment(queryset, True)


paid_for.short_description = 'Paid'


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

    actions = [status_created, status_processing, status_ready_for_pickup,
               status_shipped, status_completed, not_paid, paid_for, export_csv
               ]
