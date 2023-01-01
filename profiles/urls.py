'''imports'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('settings/', views.edit_user_settings, name='settings_edit'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
