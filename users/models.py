from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)