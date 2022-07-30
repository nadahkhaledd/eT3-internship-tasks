from django.shortcuts import render, redirect
from .models import beverage
from .forms import DrinkForm
# # Create your views here.

def home(request):
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks})

def all(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/")

    data = DrinkForm()
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks, "data": data})