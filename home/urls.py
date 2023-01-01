'''imports'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('quality/', views.quality, name='quality'),
    path('brewery/', views.brewery, name='brewery'),
    path('contact/', views.contact, name='contact'),
    path('impressum/', views.impressum, name='impressum'),
    path('agb/', views.agb, name='agb'),
]
