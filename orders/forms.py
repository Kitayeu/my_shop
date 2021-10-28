from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'telephone',
            'address', 'postal_code', 'city', 'country', 'note',
            'transport'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'email': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'address': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'city': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'country': forms.TextInput(attrs={'class': 'form-control-delivery'}),
            'note': forms.Textarea(attrs={'class': 'form-area-delivery', 'placeholder': 'Note'}),
            'transport': forms.RadioSelect()
        }
