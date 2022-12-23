'''imports'''
from django.shortcuts import (
    render, redirect, reverse
)

from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                           "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LpVxmFIoiVm8f0uYnZj7DKcnSeS7Tg967Q4xEHam1aHDCMY6d3qd5WpmHKvGd2IcqSrBRb4dBTXPhDCIH5skSGO00XjidaLlI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
