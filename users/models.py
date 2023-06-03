from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    """ref: https://dontrepeatyourself.org/post/django-custom-user-model-extending-abstractuser/"""

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password"""
        if not email:
            raise ValueError("The given email must be set! 😫")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have `is_staff=True` attribute! 🤒")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must hate `is_superuser=True` attribute! 🤒")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """unique email as a username"""

    # email field will substitute username!
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField("email address", unique=True)

    nickname = models.CharField(max_length=255)

    objects = MyUserManager()  # custom user manager

    def __str__(self) -> str:
        return self.email
