from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    BaseUserManager, PermissionsMixin
import calendar


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(
        max_length=255, unique=True, null=True, blank=True)
    fav_month = models.CharField("What is your Favorite Month", max_length=255, null=True,
                                 blank=True,
                                 choices=[(str(i), calendar.month_name[i])
                                          for i in range(1, 13)],
                                 default=calendar.month_name[1])
    family_status = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
