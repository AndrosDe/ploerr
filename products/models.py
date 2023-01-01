'''imports'''
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default='Plörr')
    description = models.TextField()
    ingredients = models.CharField(max_length=254, null=True, blank=True)
    character = models.CharField(max_length=254, null=True, blank=True)
    harmonize_with = models.CharField(max_length=254, null=True, blank=True)
    brewing_type = models.CharField(max_length=254, null=True, blank=True)
    bitter = models.CharField(max_length=254, null=True, blank=True)
    original_wort = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    alcohol_content = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    energy_100ml = models.CharField(max_length=254, null=True, blank=True)
    temperature = models.IntegerField(default=7)
    image = models.ImageField(null=True, blank=True)
    volumen = models.DecimalField(max_digits=6, decimal_places=2)
    total_volumen = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    deposit = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
