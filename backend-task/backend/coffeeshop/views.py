from django.shortcuts import render, redirect
from .models import beverage
from .forms import DrinkForm
from django.http import HttpResponse
# # Create your views here.

def base(request):
    return HttpResponse("to see all drinks -> localhost:8000/home\n  &    to add new one -> localhost:8000/add")

def add(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(base)

    return render(request, 'upload.html', {"data": DrinkForm})

def all(request):
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks})