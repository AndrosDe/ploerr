from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='calc_subweight')
def calc_subweight(volumen, quantity):
    return volumen * quantity

@register.filter(name='calc_subdeposit')
def calc_subdeposit(deposit, quantity):
    return deposit * quantity
