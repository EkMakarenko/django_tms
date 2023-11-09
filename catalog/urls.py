from django.urls import path

from catalog import views

urlpatterns = [
      path('test/', views.read_information, name='read_information'),
      path('info/', views.InfoCatalogListView.as_view(), name='info-list'),
      path('info/<int:pk>', views.InfoCatalogDetailView.as_view(), name='info-detail'),
      path('info/create', views.InfoCatalogCreateView.as_view(), name='info-create'),
      path('info/<int:pk>/update', views.InfoCatalogUpdateView.as_view(), name='info-update'),
      path('info/<int:pk>/delete', views.InfoCatalogDeleteView.as_view(), name='info-delete'),

]
