from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cf = user_form.cleaned_data
            email = cf['email']
            password = cf['password']
            password2 = cf['password2']

            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'User with given email already exists')

                    return render(
                        request,
                        'accounts/register.html',
                        {'user_form': user_form}
                    )
        else:
            messages.error(request, 'Password don\'t match')
            return render(
                request,
                'accounts/register.html',
                {'user_form': user_form}
            )
        # Create a new user object
        new_user = User.objects.create_user(
            first_name=cf['first_name'],
            last_name=cf['last_name'],
            username=cf['first_name'],
            email=email,
            password=password
        )

        Profile.objects.create(user=new_user)

        return render(request,
                      'accounts/register_done.html',
                      {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'user_form': user_form}
    )
