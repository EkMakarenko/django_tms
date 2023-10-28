from django.urls import path

from catalog import views

urlpatterns = [
      path('test/', views.read_information, name='read_information'),
      path('info/', views.InfoCatalogListView.as_view(), name='info_list'),
      path('info/<int:pk>', views.InfoCatalogDetailView.as_view(), name='info-detail'),
      # path('info/<int:pk>/update', views.PostUpdateView.as_view(), name='info-update'),
      # path('info/<int:pk>/delete', views.PostDeleteView.as_view(), name='info-delete'),
      # path('info/create', views.PostCreateView.as_view(), name='info-create'),
]
