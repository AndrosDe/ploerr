from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'total_volumen',
        'image',
        'price',
        'rating'
    )
    ordering = ('total_volumen', 'name')


admin.site.register(Product, ProductAdmin)
