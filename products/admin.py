'''imports'''
from django.contrib import admin
from .models import Product, ProductDescription, Container, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'weight_volumen',
        'price',
        'deposit',
        'rating',
    )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('weight_volumen',)


class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'category',
        'alcohol_content',
    )
    prepopulated_fields = {'product_slug': ('product_name',)}


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'units',
        'volumen_per_unit',
    )
    prepopulated_fields = {'container_slug': ('type',)}
    ordering = ('volumen_per_unit', 'units',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )
    prepopulated_fields = {'category_slug': ('category_name',)}
    ordering = ('category_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)
