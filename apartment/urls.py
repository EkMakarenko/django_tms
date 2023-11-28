from django.urls import path

from apartment import views

urlpatterns = [
    path('', views.ApartmentListView.as_view(), name='apartments'),
    path('create/', views.ApartmentCreateView.as_view(), name='apartment-create'),
]