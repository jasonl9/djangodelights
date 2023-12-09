from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("ingredient/", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/new/", views.CreateIngredientList.as_view(), name="add_ingredient"),
    path("ingredient/<pk>/delete/", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path("menuitem/", views.MenuItemList.as_view(), name="menuitemlist"),
    path("menuitem/new/", views.CreateMenuItemList.as_view(), name="add_menuitem"),
    path("reciperequirement/", views.RecipeRequirementList.as_view(), name="reciperequirementlist"),
    path("reciperequirement/new/", views.CreateRecipeRequirementList.as_view(), name="add_reciperequirement"),
    path("purchase/", views.PurchaseList.as_view(), name="purchaselist"),
    path("purchase/new/", views.CreatePurchaseList.as_view(), name="add_purchase")
]