from django.contrib import admin

# Register your models here.

from django.contrib import admin
from users.models import UserProfile

admin.site.register(UserProfile)