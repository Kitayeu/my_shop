from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control-cart'}), min_value=1
    )
