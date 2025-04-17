from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)  # Fixed typo from is_activate
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"  # Changed from plural to singular
    REQUIRED_FIELDS = ["name"]

    def __str__(self):  # Fixed from three underscores to two
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
