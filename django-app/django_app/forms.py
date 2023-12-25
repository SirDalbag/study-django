from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # price = forms.DecimalField()
    # image = forms.ImageField()
    class Meta:
        model = Product
        fields = ["name", "price", "image"]
