from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from info.models import InfoHotelCatalog


# Create your views here.

#
def read_information(request):
    return render(request, 'index.html')
#
#
def read_catalog(request):
    return render(request, 'catalog.html')
#
#
# def read_details(request):
#     return render(request, 'details.html')
# #

# def read_comments(request):
#     return render(request, 'comments.html')


class CommentsView(View):
    def get(self, request):
        amount_comments = InfoHotelCatalog.objects.filter(is_deleted=False).count()
        # print(catalogs.values_list())
        print(amount_comments)
        return render(request, 'index.html', context={'amount_comments': amount_comments})

print()