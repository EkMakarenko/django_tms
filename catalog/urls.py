from django.urls import path

from catalog import views

urlpatterns = [
      path('test/', views.read_information, name='read_information'),
      path('catalog', views.read_catalog, name='read_catalog'),
      # path('comments', views.read_comments, name='read_comments'),
]
