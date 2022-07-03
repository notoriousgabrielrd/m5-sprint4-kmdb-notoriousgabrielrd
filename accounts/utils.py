from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,first_name,last_name,**extra_fields):

        if not email:
            raise ValueError("O email é obrigatório.")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff = True,
            is_active = True,
            is_superuser = False,
            date_joined = timezone.now(),
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,email,password,first_name,last_name,**extra_fields):

        if not email:
            raise ValueError("O email é obrigatório.")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff = True,
            is_active = True,
            is_superuser = True,
            date_joined = timezone.now(),
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user