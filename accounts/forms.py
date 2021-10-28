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
            'first_name': forms.TextInput(attrs={'class': 'form_user_update'}),
            'last_name': forms.TextInput(attrs={'class': 'form_user_update'}),
            'email': forms.EmailInput(attrs={'class': 'form_user_update'})
        }


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone_number', 'address', 'postal_code', 'city', 'country')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form_user_update'}),
            'address': forms.TextInput(attrs={'class': 'form_user_update'}),
            'postal_code': forms.TextInput(attrs={'class': 'form_user_update'}),
            'city': forms.TextInput(attrs={'class': 'form_user_update'}),
            'country': forms.TextInput(attrs={'class': 'form_user_update'})
        }
