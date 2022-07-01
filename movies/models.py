

# Create your models here.



# from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     updated_at = models.DateTimeField(auto_now=True)
#     date_joined = models.DateTimeField()
#     username = models.CharField(unique=False, null=True, max_length=55)
#     # username = None
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["first_name","last_name"]

#     objects = CustomUserManager()


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.CharField(max_length=20)
    synopsis = models.TextField()

    genres = models.ManyToManyField("genres.Genre", related_name="movies")

    