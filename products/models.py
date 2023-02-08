'''imports'''
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import Avg


class Category(models.Model):
    ''' Product Category '''
    class Meta:
        '''Category Model Meta'''
        verbose_name_plural = "Categories"

    category_name = models.CharField(max_length=254)
    category_slug = models.SlugField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the slug automatically.
        """
        self.category_slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class ProductDescription(models.Model):
    ''' Product Information '''
    product_name = models.CharField(max_length=254)
    product_slug = models.SlugField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="categories")
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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the slug automatically.
        """
        self.product_slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Container(models.Model):
    ''' Container Data '''
    type = models.CharField(max_length=254)
    container_slug = models.SlugField(max_length=254, null=True, blank=True)
    units = models.IntegerField(default=1)
    size = models.CharField(max_length=254, null=True, blank=True)
    volumen_per_unit = models.DecimalField(
        default=0, max_digits=6, decimal_places=3)
    deposit_per_unit = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the slug automatically.
        """
        self.container_slug = slugify(self.type)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class Product(models.Model):
    ''' Product Item Data '''
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, null=True, blank=True)
    product_description = models.ForeignKey(ProductDescription, null=True,
                                            on_delete=models.CASCADE,
                                            related_name="products")
    container = models.ForeignKey(Container, null=True,
                                  on_delete=models.CASCADE,
                                  related_name="containers")
    image = models.ImageField(null=True, blank=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, null=False, default=0)
    volumen = models.DecimalField(
        max_digits=6, decimal_places=3,
        null=False, blank=False, editable=False)
    weight_volumen = models.DecimalField(
        max_digits=6, decimal_places=3,
        null=False, blank=False, editable=False)
    deposit = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def update(self):
        """
        Updating when a reivew was made or something changed with the container
        """
        self.rating = self.productreview.aggregate(
            Avg('user_rating'))['user_rating__avg'] or None

        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item weight, deposit
        and slug automatically.
        """
        self.volumen = self.container.volumen_per_unit * self.container.units
        self.weight_volumen = self.volumen + self.weight
        self.deposit = self.container.deposit_per_unit * self.container.units
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_name(self):
        return self.name


class UserReview(models.Model):
    ''' Product User Review Data '''
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name="productreview")
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE,
                             related_name="userreviews")
    user_rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'''
        {self.user.username} on product {self.product.name}
        '''
