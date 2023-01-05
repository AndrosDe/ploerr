'''imports'''
from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def quality(request):
    """ A view to return the quality page """
    return render(request, 'home/quality.html')


def brewery(request):
    """ A view to return the brewery page """
    return render(request, 'home/brewery.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')


def impressum(request):
    """ A view to return the imprint page """
    return render(request, 'home/impressum.html')


def privacypolicy(request):
    """ A view to return the privacypolicy page """
    return render(request, 'home/privacypolicy.html')


def agb(request):
    """ A view to return the GTC page """
    return render(request, 'home/agb.html')