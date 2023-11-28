from django.contrib import admin

from catalog.models import HotelCatalog

# admin.site.register(HotelCatalog)

# Register your models here.


@admin.register(HotelCatalog)
class HotelCatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'city', 'street', 'house_number', 'description', 'rating')
    list_filter = ('rating', 'name', 'country', 'city')
    search_fields = ('name', 'rating', 'city')
    sortable_by = ('price', 'rating', 'name', 'country', 'city')
