from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()

# Create your models here.
