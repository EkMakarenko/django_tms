from django.db import models

from catalog.models import HotelCatalog


# Create your models here.


class Apartment(models.Model):
    # hotel_id = models.ForeignKey()
    total_area = models.PositiveIntegerField(name=False)
    numer_of_bedrooms = models.BooleanField(null=False, default=False)
    price = models.PositiveIntegerField(name=False)
    is_deleted = models.BooleanField(null=False, default=False)
