from django.contrib import admin

from info.models import InfoHotelCatalog

admin.site.register(InfoHotelCatalog)
# Register your models here.


# @admin.register(InfoHotelCatalog)
# class InfoHotelCatalogAdmin(admin.ModelAdmin):
#     list_display = {'id', 'name', 'description', 'rating'}
#     list_filter = {'rating'}
#     search_fields = {'name', 'rating'}
#     sortable_by = {'price', 'rating'}
