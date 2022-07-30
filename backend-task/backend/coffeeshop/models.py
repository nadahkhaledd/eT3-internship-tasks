from django.db import models


class beverage(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=350)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    size = models.CharField(max_length=300)
    ingredients = models.CharField(max_length=500)
