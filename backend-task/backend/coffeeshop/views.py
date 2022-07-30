from django.shortcuts import render, redirect
from .models import beverage
from .forms import DrinkForm
from django.http import HttpResponse
# # Create your views here.

def base(request):
    return HttpResponse("ok")

def all(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(base)

    data = DrinkForm()
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks, "data": data})