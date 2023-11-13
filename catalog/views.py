from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View

from catalog.form import InfoHotelCatalogForm
from catalog.models import HotelCatalog
from comment.form import CommentForm


# Create your views here.

#
def read_information(request):
    return render(request, 'index.html')


# class InfoCatalogView(View):
#     def get(self, request, id=None):
#         info = HotelCatalog.objects.all()
#
#         if id:
#             information = HotelCatalog.objects.get(id=id, is_deleted=False)
#             return render(request, 'info.html', context={'info': info, 'information': information })
#
#         return render(request, 'index.html', context={'info': info})

class InfoCatalogListView(generic.ListView):
    template_name = 'info_catalog/info_list.html'
    context_object_name = 'info'
    queryset = HotelCatalog.objects.filter(is_deleted=False)


class InfoCatalogDetailView(generic.DetailView):
    model = HotelCatalog
    template_name = 'info_catalog/info_detail.html'
    context_object_name = 'info_detail'
    # form = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = HotelCatalog.objects.filter(is_deleted=False)
        return context


class InfoCatalogCreateView(generic.CreateView):
    template_name = 'info_catalog/info_create.html'
    form_class = InfoHotelCatalogForm

    def get_success_url(self):
        return reverse('info-list')


class InfoCatalogUpdateView(generic.UpdateView):
    model = HotelCatalog
    template_name = 'info_catalog/info_update.html'
    form_class = InfoHotelCatalogForm

    def get_success_url(self):
        return reverse('info-list')


class InfoCatalogDeleteView(generic.DeleteView):
    model = HotelCatalog
    template_name = 'info_catalog/info_delete.html'

    def get_success_url(self):
        return reverse('info-list')

