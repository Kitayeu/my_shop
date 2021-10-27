from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'form_user_registration'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First name', 'class': 'form_user_registration'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last name', 'class': 'form_user_registration'},
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email', 'class': 'form_user_registration'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password', 'class': 'form_user_registration'}
            ),
        }


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput()
        }


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone_number', 'address', 'postal_code', 'city', 'country')
        widgets = {
            'phone_number': forms.TextInput(),
            'address': forms.TextInput(),
            'postal_code': forms.TextInput(),
            'city': forms.TextInput(),
            'country': forms.TextInput()
        }
