'''imports'''
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    weight = 0
    product_count = 0
    shipping_cost = 0
    total_deposit = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        weight += quantity * product.total_volumen
        total_deposit += quantity * product.deposit
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if weight >= 5:
        if weight >= 10:
            if weight >= 31:
                if weight >= 50:
                    shipping_cost = 30
                else:
                    shipping_cost = 16
            else:
                shipping_cost = 9
        else:
            shipping_cost = 5
    else:
        shipping_cost = 0

    grand_total = total + shipping_cost + total_deposit

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'weight': weight,
        'shipping_cost': shipping_cost,
        'total_deposit': total_deposit,
        'grand_total': grand_total,
    }

    return context
