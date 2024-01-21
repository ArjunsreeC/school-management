# urls.py

from django.urls import path
from .views import home_view, registration_view, my_protected_view
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', registration_view, name='register'),
    path('login/', LoginView.as_view(template_name='custom_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', my_protected_view, name='protected_view'),
]
