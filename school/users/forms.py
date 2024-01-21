from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=255)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    country = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
