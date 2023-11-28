from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class HotelCatalog (models.Model):
    name = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    street = models.CharField(max_length=20, null=False)
    house_number = models.CharField(max_length=20, null=False)
    description = models.TextField()

    rating = models.FloatField(name=False, validators=[MinValueValidator(1.), MaxValueValidator(10.)])
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name
