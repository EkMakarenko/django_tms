from django.contrib import admin

from apartment.models import Apartment
from catalog.models import HotelCatalog

# Register your models here.

# admin.site.register(Apartment)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_area', 'numer_of_bedrooms', 'number_of_bathroom', 'hotel_id', 'price')
    list_filter = ('total_area', 'price')
    search_fields = ['price']
    sortable_by = ('price', 'total_area')
