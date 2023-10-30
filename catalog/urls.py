from django.urls import path

from catalog import views

urlpatterns = [
      path('test/', views.read_information, name='read_information'),
      path('info/', views.InfoCatalogView.as_view(), name='info'),
      path('info/<int:id>', views.InfoCatalogView.as_view(), name='information')
]
