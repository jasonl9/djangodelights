from django.shortcuts import render

# Create your views here.
from .models import Ingredient
from django.views.generic import ListView


class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"