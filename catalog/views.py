from gettext import Catalog

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from catalog.models import HotelCatalog


# Create your views here.

#
def read_information(request):
    return render(request, 'index.html')


class InfoCatalogView(View):
    def get(self, request, id=None):
        info = HotelCatalog.objects.all()

        if id:
            information = HotelCatalog.objects.get(id=id, is_deleted=False)
            return render(request, 'info.html', context={'info': info, 'information': information})

        return render(request, 'index.html', context={'info': info})
