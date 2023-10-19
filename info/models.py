from django.db import models


class InfoHotelCatalog (models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField()
    rating = models.PositiveIntegerField(name=False)
    is_deleted = models.BooleanField(null=False, default=False)

