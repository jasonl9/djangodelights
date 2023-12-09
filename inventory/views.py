from django.shortcuts import render

# Create your views here.
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm

class HomeView(TemplateView):
    template_name = "inventory/home.html"

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class CreateIngredientList(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/add_ingredient.html"

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/inventory/ingredient"

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class CreateMenuItemList(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/add_menuitem.html"

class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_list.html"

class CreateRecipeRequirementList(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/add_reciperequirement.html"

class PurchaseList(TemplateView):
    template_name = "inventory/purchase_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.order_by("timestamp")
        context["menuitems"] = MenuItem.objects.all()
        return context

class CreatePurchaseList(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/add_purchase.html"