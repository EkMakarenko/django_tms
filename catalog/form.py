from django import forms

from catalog.models import HotelCatalog


class InfoHotelCatalogForm(forms.ModelForm):
    class Meta:
        model = HotelCatalog
        fields = ('id', 'name', 'country', 'city', 'street', 'house_number', 'description', 'rating')
