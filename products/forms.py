'''Imports'''
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, ProductDescription, Container, UserReview


class ProductForm(forms.ModelForm):
    ''' The Form for the Products '''
    class Meta:
        model = Product
        fields = (
            'name',
            'product_description',
            'container',
            'image',
            'price',
            'weight',
            )
        labels = {
            'weight': 'Weight of the Products solid Components',
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-3'


class ProductDescriptionForm(forms.ModelForm):
    ''' The Form for the Products Description'''
    class Meta:
        model = ProductDescription
        fields = (
            'product_name',
            'description',
            'category',
            'ingredients',
            'character',
            'harmonize_with',
            'brewing_type',
            'alcohol_content',
            'bitter',
            'original_wort',
            'energy_100ml',
            'temperature',
            )

        labels = {
            'product_name': 'Product Name',
            'harmonize_with': 'Goes well with',
            'energy_100ml': 'Energy on 100ml',
            'temperature': 'Drinking Temperature',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-3'


class ContainerForm(forms.ModelForm):
    ''' The Form for the Products Container'''
    class Meta:
        model = Container
        fields = (
            'type',
            'units',
            'volumen_per_unit',
            'deposit_per_unit',
            'size',
            )

        labels = {
            'size': 'Product / Container Size',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-3'


class UserReviewForm(forms.ModelForm):
    ''' The Form for the UserReview'''
    class Meta:
        model = UserReview
        fields = (
            'user_rating',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-3'
