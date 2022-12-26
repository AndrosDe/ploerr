"""Imports"""
import uuid

from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    weight_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    deposit_total = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for shipping costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        self.deposit_total = self.lineitems.aggregate(
            Sum('lineitem_total_deposit'))['lineitem_total_deposit__sum'] or 0

        self.weight_total = self.lineitems.aggregate(
            Sum('lineitem_total_weight'))['lineitem_total_weight__sum'] or 0

        if self.weight_total >= 5:
            if self.weight_total >= 10:
                if self.weight_total >= 31:
                    if self.weight_total >= 50:
                        self.shipping_cost = 30
                    else:
                        self.shipping_cost = 16
                else:
                    self.shipping_cost = 9
            else:
                self.shipping_cost = 5
        else:
            self.shipping_cost = 0

        self.grand_total = (
            self.order_total + self.deposit_total + self.shipping_cost
            )
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total_price = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    lineitem_total_deposit = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    lineitem_total_weight = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total lines
        and update the order total.
        """
        self.lineitem_total_price = self.product.price * self.quantity
        self.lineitem_total_deposit = self.product.deposit * self.quantity
        self.lineitem_total_weight = self.product.total_volumen * self.quantity
        self.lineitem_total = (
            self.lineitem_total_price + self.lineitem_total_deposit
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'''
        {self.product.friendly_name} on order {self.order.order_number}
        '''
