'''imports'''
from django.contrib import admin
from .models import Item, Product, Container


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'product',
        'container',
        'weight',
        'price',
        'deposit',
        'rating'
    )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('weight',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'alcohol_content',
    )


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'volumen_per_unit',
    )
    ordering = ('volumen_per_unit',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Item, ItemAdmin)
