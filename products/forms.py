'''Imports'''
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, ProductDescription, Container


class ProductForm(forms.ModelForm):
    ''' The Form for the Products '''
    rating = forms.DecimalField(
        label="Rate Product from 0 to 5", required=False)
    weight = forms.DecimalField(
        label="Weight of the Products solid components")

    class Meta:
        model = Product
        fields = (
            'name',
            'product_description',
            'container',
            'image',
            'rating',
            'price',
            'weight',
            )

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-3'
