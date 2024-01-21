from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import UserProfile
from .forms import UserRegistrationForm

def home_view(request):
    return render(request, 'home.html', context={})


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            country = form.cleaned_data['country']
            nationality = form.cleaned_data['nationality']
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']

            user = UserProfile.objects.create_user(email, name, role, country, nationality, mobile, password)

            # Redirect to a success page or home page
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})



def custom_login(request, **kwargs):
    return render(request, 'custom_login.html', context={})


def my_protected_view(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user_role = request.user.userprofile.role
            print(user_role,"..............................")
        return render(request, 'my_protected_view.html', {'user_role': user_role})
    else:
        # Handle the case where the user is not logged in
        return render(request, 'not_logged_in_template.html', {})