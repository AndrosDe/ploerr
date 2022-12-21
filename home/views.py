'''imports'''
from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def quality(request):
    """ A view to return the index page """
    return render(request, 'home/quality.html')


def brewery(request):
    """ A view to return the index page """
    return render(request, 'home/brewery.html')


def contact(request):
    """ A view to return the index page """
    return render(request, 'home/contact.html')


def impressum(request):
    """ A view to return the index page """
    return render(request, 'home/impressum.html')


def agb(request):
    """ A view to return the index page """
    return render(request, 'home/agb.html')
