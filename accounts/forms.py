from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last name'},
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
        }
