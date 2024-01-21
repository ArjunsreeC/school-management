from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, role, country, nationality, mobile, password=None):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = User(email=email)
        user.set_password(password)
        user.save(using=self._db)

        profile = self.model(user=user, name=name, role=role, country=country, nationality=nationality, mobile=mobile)
        profile.save(using=self._db)

        return user

    def create_superuser(self, email, name, role, country, nationality, mobile, password=None):
        user = self.create_user(email, name, role, country, nationality, mobile, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    STUDENT = 'student'
    STAFF = 'staff'
    ADMIN = 'admin'
    EDITOR = 'editor'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
        (EDITOR, 'Editor'),
    ]

    objects = UserProfileManager()  # Add this line to use the custom manager

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)

    USERNAME_FIELD = 'user'  # Change this to 'user' as it is a OneToOneField to User model
    REQUIRED_FIELDS = ['name', 'role', 'country', 'nationality', 'mobile']  # Add the required fields

    def __str__(self):
        return self.user.email