from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique=True,
        blank = False
    )
    description = models.CharField(
        max_length = 120,
        unique = False,
        blank = True
    )
    quantity = models.IntegerField(
        unique = False,
        validators = [MinValueValidator(0, "Quantity must not be less than 0"),
        MaxValueValidator(100, "Quantity must not be more than 100")]
    )
