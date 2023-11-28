from django import forms

from apartment.models import Apartment


class ApartmentForm(forms.ModelForm):
    # apartment_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Apartment
        fields = ('total_area', 'numer_of_bedrooms', 'number_of_bathroom', 'price', 'hotel_id')
