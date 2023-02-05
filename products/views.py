'''imports'''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, ProductDescription, Container, Category
from .forms import ProductForm, ProductDescriptionForm, ContainerForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all().order_by('weight_volumen')
    categories = Category.objects.all().order_by('category_name')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def category_filter(request, category_id):

    categories = Category.objects.all().order_by('category_name')
    filter = Category.objects.filter(id=category_id)
    for category in filter:
        category_filter = category

    products = Product.objects.filter(
        product_description__category=category_id)

    context = {
        'products': products,
        'category_filter': category_filter,
        'categories': categories,
    }

    return render(request, 'products/category_filter.html', context)


# ------ Products Management Views ------ #
# 1. Overview
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


# 2. Adding Products, Product Descriptions & Containers
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


# 3. Update Products, Product Descriptions & Containers
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product)
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
def edit_description(request, description_id):
    """ Edit a description in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    description = get_object_or_404(ProductDescription, pk=description_id)
    if request.method == 'POST':
        form = ProductDescriptionForm(
            request.POST,
            request.FILES,
            instance=description)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated description!')
            return redirect(reverse('all_descriptions'))
        else:
            messages.error(request,
                           ('Failed to update the description. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductDescriptionForm(instance=description)
        messages.info(request, f'You are editing {description.product_name}')

    template = 'products/edit_description.html'
    context = {
        'form': form,
        'description': description,
    }

    return render(request, template, context)


@login_required
def edit_container(request, container_id):
    """ Edit a container in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    container = get_object_or_404(Container, pk=container_id)
    if request.method == 'POST':
        form = ContainerForm(
            request.POST,
            request.FILES,
            instance=container)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated container!')
            return redirect(reverse('all_containers'))
        else:
            messages.error(request,
                           ('Failed to update the container. '
                            'Please ensure the form is valid.'))
    else:
        form = ContainerForm(instance=container)
        messages.info(request, f'You are editing {container.type}')

    template = 'products/edit_container.html'
    context = {
        'form': form,
        'container': container,
    }

    return render(request, template, context)


# 4. Deleting Products, Product Descriptions & Containers
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


@login_required
def delete_description_confirm(request, description_id):
    """ A view to confirm description deletion """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    description = get_object_or_404(ProductDescription, pk=description_id)

    context = {
        'description': description,
    }

    return render(request, 'products/confirm_delete_description.html', context)


@login_required
def delete_description(request, description_id):
    """ Delete a description from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    description = get_object_or_404(ProductDescription, pk=description_id)
    description.delete()
    messages.success(request, 'Description deleted!')
    return redirect(reverse('all_descriptions'))


@login_required
def delete_container_confirm(request, container_id):
    """ A view to confirm container deletion """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    container = get_object_or_404(Container, pk=container_id)

    context = {
        'container': container,
    }

    return render(request, 'products/confirm_delete_container.html', context)


@login_required
def delete_container(request, container_id):
    """ Delete a container from the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    container = get_object_or_404(Container, pk=container_id)
    container.delete()
    messages.success(request, 'Container deleted!')
    return redirect(reverse('all_containers'))
