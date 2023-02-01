'''imports'''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm


def all_products(request):
    """ A view to show all products """

    products = Item.objects.all().order_by('weight')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_item_id):
    """ A view to show individual product details """

    product_item = get_object_or_404(Item, pk=product_item_id)

    context = {
        'product_item': product_item,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            product_item = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product_item.id]))
        else:
            messages.error(request,
                           ('Failed to update the product. '
                            'Please ensure the form is valid.'))
    else:
        form = ItemForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_item_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_item = get_object_or_404(Item, pk=product_item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=product_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product_item.id]))
        else:
            messages.error(request,
                           ('Failed to update the product. '
                            'Please ensure the form is valid.'))
    else:
        form = ItemForm(instance=product_item)
        messages.info(request, f'You are editing {product_item.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product_item': product_item,
    }

    return render(request, template, context)


@login_required
def delete_product_confirm(request, product_item_id):
    """ A view to confirm product deletion """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_item = get_object_or_404(Item, pk=product_item_id)

    context = {
        'product_item': product_item,
    }

    return render(request, 'products/confirm_delete.html', context)


@login_required
def delete_product_item(request, product_item_id):
    """ Delete a product from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product_item = get_object_or_404(Item, pk=product_item_id)
    product_item.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
