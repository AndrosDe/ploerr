'''imports'''
from django.urls import path
from . import views

urlpatterns = [
     path('',
          views.all_products,
          name='products'),
     path('<int:product_id>/',
          views.product_detail,
          name='product_detail'),
     path('management/',
          views.products_management,
          name='products_management'),
     path('add/',
          views.add_product,
          name='add_product'),
     path('edit/<int:product_id>/',
          views.edit_product,
          name='edit_product'),
     path('delete/<int:product_id>/',
          views.delete_product,
          name='delete_product'),
     path('confirm/delete/<int:product_id>/',
          views.delete_product_confirm,
          name='confirm_delete'),
]
