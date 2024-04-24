from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    account_type = models.CharField(max_length=255)