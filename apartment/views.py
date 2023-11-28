from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from apartment.form import ApartmentForm
from apartment.models import Apartment
from catalog.models import HotelCatalog
from comment.form import CommentForm


# Create your views here.

class ApartmentListView(generic.ListView):
    template_name = 'apartment/apartment_list.html'
    context_object_name = 'apartments'
    queryset = Apartment.objects.all()


class ApartmentDetailView(generic.DetailView):
    model = HotelCatalog
    template_name = 'apartment/apartment_detail.html'
    context_object_name = 'apartment_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Apartment.objects.filter(is_deleted=False)
        return context


class ApartmentCreateView(generic.CreateView):
    template_name = 'apartment/apartment_create.html'
    form_class = ApartmentForm

    def get_success_url(self):
        return reverse('apartments')

    def form_valid(self, form):
        form.instance.apartment_id = self.kwargs.get('apartment_id')
        return super().form_valid(form)
