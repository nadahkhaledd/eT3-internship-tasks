from django.shortcuts import render, redirect
from .models import beverage
from .forms import DrinkForm
# # Create your views here.

def all(request):
    if request.method == "POST":
        form = DrinkForm(request.POST)
        if form.is_valid():
            drink = form.save(commit=False)
            drink.bevarage = request.beverage
            drink.save()
            return redirect("home/")

    data = DrinkForm()
    drinks = beverage.objects.all()
    return render(request, 'home.html', {'drinks': drinks, "data": data})