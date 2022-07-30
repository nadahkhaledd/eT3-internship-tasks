from django.shortcuts import render
from .models import beverage
# # Create your views here.

def all(request):
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks})

