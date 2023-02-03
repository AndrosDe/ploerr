'''imports'''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, ProductDescription, Container
from .forms import ProductForm, ProductDescriptionForm, ContainerForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all().order_by('weight_volumen')

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def products_management(request):
    """ A view to return the products_management page """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    return render(request, 'products/products_management.html')


def all_descriptions(request):
    """ A view to show all product descriptions """

    descriptions = ProductDescription.objects.all().order_by(
        'product_name', 'category')

    context = {
        'descriptions': descriptions,
    }

    return render(request, 'products/descriptions.html', context)


def all_containers(request):
    """ A view to show all containers """

    containers = Container.objects.all().order_by('volumen_per_unit', 'units')

    context = {
        'containers': containers,
    }

    return render(request, 'products/containers.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update the product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_description(request):
    """ Add a description for a product """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductDescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.save()
            messages.success(request, 'Successfully added description!')
            return redirect(reverse(
                'all_descriptions'))
        else:
            messages.error(request,
                           ('Failed to update the description. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductDescriptionForm()

    template = 'products/add_description.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_container(request):
    """ Add a container for a product """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ContainerForm(request.POST, request.FILES)
        if form.is_valid():
            container = form.save()
            messages.success(request, 'Successfully added container!')
            return redirect(reverse(
                'all_containers'))
        else:
            messages.error(request,
                           ('Failed to update the container. '
                            'Please ensure the form is valid.'))
    else:
        form = ContainerForm()

    template = 'products/add_container.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update the product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product_confirm(request, product_id):
    """ A view to confirm product deletion """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/confirm_delete_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
