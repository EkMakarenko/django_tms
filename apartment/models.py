from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from catalog.models import HotelCatalog


# Create your models here.


class Apartment(models.Model):
    hotel_id = models.ForeignKey(HotelCatalog, on_delete=models.CASCADE, related_name='apartments')
    total_area = models.PositiveIntegerField(name=False)
    numer_of_bedrooms = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1.), MaxValueValidator(5.)])
    number_of_bathroom = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1.), MaxValueValidator(5.)])
    price = models.PositiveIntegerField(name=False)
    is_deleted = models.BooleanField(null=False, default=False)
