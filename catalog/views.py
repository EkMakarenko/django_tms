from django.shortcuts import render
from django.views import generic

from catalog.models import HotelCatalog


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
#             return render(request, 'info.html', context={'info': info, 'information': information})
#
#         return render(request, 'index.html', context={'info': info})

class InfoCatalogListView(generic.ListView):
    template_name = 'info_catalog/info_list.html'
    context_object_name = 'info'
    queryset = HotelCatalog.objects.filter(is_deleted=False)


class PostCreateView(generic.CreateView):
    pass
#     # model = InfoBlog
#     template_name = 'info_blog/post_create.html'
#     form_class = InfoBlogForm
#     # fields = ('name', 'text', 'rating', 'price')
#     # success_url = '/blog/posts/'
#
#     def get_success_url(self):
#         return reverse('post-list')


class InfoCatalogDetailView(generic.DetailView):
    pass
    model = HotelCatalog
    template_name = 'info_catalog/info_detail.html'
    context_object_name = 'info'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = InfoBlog.objects.filter(is_deleted=False)
#         # print(50*'-')
#         # print(context['posts'].values()[0]['name'])
#         # print(context['posts'].query)
#         # print(50*'-')
#         return context
#
#
class PostUpdateView(generic.UpdateView):
    pass
#     model = InfoBlog
#     template_name = 'info_blog/post_update.html'
#     form_class = InfoBlogForm
#
#     def get_success_url(self):
#         return reverse('post-list')
#
#
class PostDeleteView(generic.DeleteView):
    pass