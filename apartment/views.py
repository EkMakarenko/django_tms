from django.shortcuts import render

# Create your views here.


def read_apartment(request):
    return render(request, 'apartment.html')