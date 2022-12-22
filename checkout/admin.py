'''imports'''
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'lineitem_total', 'lineitem_total_price',
        'lineitem_total_deposit', 'lineitem_total_weight')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'weight_total', 'grand_total')

    fields = ('order_number', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'weight_total', 'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_total', 'shipping_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
