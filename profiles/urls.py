from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('settings/', views.edit_user_settings, name='settings_edit'),
]
