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
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.TextInput(),
            'telephone': forms.TextInput(),
            'address': forms.TextInput(),
            'postal_code': forms.TextInput(),
            'city': forms.TextInput(),
            'country': forms.TextInput(),
            'note': forms.Textarea(),
            'transport': forms.RadioSelect()
        }
