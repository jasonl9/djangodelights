from django.shortcuts import render

# Create your views here.
from .models import Ingredient, MenuItem, Purchase
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from .forms import IngredientForm


class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/inventory/ingredient"

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"