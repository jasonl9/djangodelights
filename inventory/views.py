from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def logout_view(request):
    logout(request)
    return redirect("login")

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class CreateIngredientList(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/add_ingredient.html"

class UpdateIngredientList(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/update_ingredient.html"

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/inventory/ingredient"

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class CreateMenuItemList(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/add_menuitem.html"

class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_list.html"

class CreateRecipeRequirementList(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = "inventory/add_reciperequirement.html"

class PurchaseList(LoginRequiredMixin, TemplateView):
    template_name = "inventory/purchase_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.order_by("timestamp")
        context["menuitems"] = MenuItem.objects.all()
        return context

class CreatePurchaseList(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/add_purchase.html"