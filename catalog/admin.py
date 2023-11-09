from django.contrib import admin

from catalog.models import HotelCatalog

# admin.site.register(HotelCatalog)

# Register your models here.


@admin.register(HotelCatalog)
class HotelCatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'description', 'rating')
    list_filter = ('rating', 'name', 'country')
    search_fields = ('name', 'rating')
    sortable_by = ('price', 'rating', 'name', 'country')
