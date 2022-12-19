from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    weight = 0
    product_count = 0
    shipping_cost = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        weight += quantity * product.total_volumen
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if weight == 0:
        shipping_cost = 0
    elif weight < 5:
        shipping_cost = 5
    elif weight < 10:
        shipping_cost = 9
    elif weight < 31:
        shipping_cost = 16
    elif weight < 50:
        shipping_cost = 30

    grand_total = total + shipping_cost

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'weight': weight,
        'shipping_cost': shipping_cost,
        'grand_total': grand_total,
    }

    return context
