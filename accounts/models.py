
from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import CustomUserManager
from django.utils import timezone 

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField()
    username = models.CharField(unique=False, null=True, max_length=55)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]

    objects = CustomUserManager()
