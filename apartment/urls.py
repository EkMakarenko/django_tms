from django.urls import path

from apartment import views

urlpatterns = [
      path('apartment', views.read_apartment, name='read_apartment')
]