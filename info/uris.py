from django.urls import path

from info import views

urlpatterns = [
      path('test/', views.read_information, name='read_information'),
      # path('catalog', views.read_catalog, name='read_details'),
      # path('comments', views.read_comments, name='read_comments'),
]
