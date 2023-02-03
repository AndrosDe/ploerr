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
    search_fields = ['price', 'weight_volumen']
    list_filter = ('weight_volumen',)
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'image',)}),
        (('Select Product'), {'fields': ('product_description',)}),
        (('Select Container'), {'fields': ('container',)}),
        (('Price & Rating'), {'fields': ('price', 'rating',)}),
        (('Enter weight of any solid component'), {'fields': ('weight',)}),
    )


class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'category',
        'alcohol_content',
    )
    prepopulated_fields = {'product_slug': ('product_name',)}
    ordering = ('product_name', 'category',)
    search_fields = ['category']
    list_filter = ('category',)
    fieldsets = (
        (None, {'fields': ('product_name', 'product_slug', 'description',)}),
        (('Select Category'), {'fields': ('category',)}),
        (('Optional Description'), {'fields': (
            'ingredients', 'character', 'harmonize_with', 'brewing_type',)}),
        (('Details'), {'fields': (
            'alcohol_content', 'bitter', 'original_wort',
            'energy_100ml', 'temperature',)}),
    )


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'units',
        'volumen_per_unit',
    )
    prepopulated_fields = {'container_slug': ('type',)}
    ordering = ('volumen_per_unit', 'units',)
    search_fields = ['type']
    list_filter = ('units', 'volumen_per_unit',)
    fieldsets = (
        (None, {'fields': ('type', 'container_slug',)}),
        (('Container Details'), {'fields': (
            'units', 'volumen_per_unit', 'deposit_per_unit',)}),
        (('Product / Container Size'), {'fields': ('size',)}),
    )


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
