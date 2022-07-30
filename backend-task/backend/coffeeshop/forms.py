from django import forms
from .models import beverage

class DrinkForm(forms.ModelForm):
    name = forms.CharField(required=True,
            widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Drink name",
                "class": "textinput is-success is-medium",
            }
        ),
        label="Drink name",)

    category = forms.CharField(required=True,
            widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "category",
                "class": "textinput is-success is-medium",
            }
        ),
        label="Category",)
    price = forms.FloatField(required=True,
            widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "price",
                "class": "textinput is-success is-medium",
            }
        ),
        label="Price",)

    size = forms.RadioSelect(choices=['Tall', 'Grande', 'Venti'])

    class Meta:
        model = beverage
        exclude = ['ingredients']