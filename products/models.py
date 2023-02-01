'''imports'''
from django.db import models


class Product(models.Model):
    ''' Product Information '''
    product_name = models.CharField(max_length=254)
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
    temperature = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Container(models.Model):
    ''' Container  Data '''
    type = models.CharField(max_length=254)
    units = models.IntegerField(default=1)
    size = models.CharField(max_length=254, null=True, blank=True)
    volumen_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    deposit_per_unit = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.type


class Item(models.Model):
    ''' Product Item Data '''
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    product = models.ForeignKey(Product, null=True,
                                on_delete=models.CASCADE,
                                related_name="products")
    container = models.ForeignKey(Container, null=True,
                                  on_delete=models.CASCADE,
                                  related_name="containers")
    image = models.ImageField(null=True, blank=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    deposit = models.DecimalField(
        default=0, max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item weight and deposit
        automatically.
        """
        self.weight = self.container.volumen_per_unit * self.container.units
        self.deposit = self.container.deposit_per_unit * self.container.units
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_name(self):
        return self.name
