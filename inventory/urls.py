from django.urls import path, include

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    #login path is 'inventory/account/login' although here it says 'account/', dont know why
    path("account/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("ingredient/", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/new/", views.CreateIngredientList.as_view(), name="add_ingredient"),
    path("ingredient/<pk>/update/", views.UpdateIngredientList.as_view(), name="update_ingredient"),
    path("ingredient/<pk>/delete/", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path("menuitem/", views.MenuItemList.as_view(), name="menuitemlist"),
    path("menuitem/new/", views.CreateMenuItemList.as_view(), name="add_menuitem"),
    path("menuitem/<pk>/update/", views.UpdateMenuItemList.as_view(), name="update_menuitem"),
    path("menuitem/<pk>/delete/", views.DeleteMenuItemList.as_view(), name="delete_menuitem"),
    path("reciperequirement/", views.RecipeRequirementList.as_view(), name="reciperequirementlist"),
    path("reciperequirement/new/", views.CreateRecipeRequirementList.as_view(), name="add_reciperequirement"),
    path("reciperequirement/<pk>/update", views.UpdateRecipementRequirementList.as_view(), name="update_reciperequirement"),
    path("reciperequirement/<pk>/delete", views.DeleteRecipeRequirementList.as_view(), name="delete_reciperequirement"),
    path("purchase/", views.PurchaseList.as_view(), name="purchaselist"),
    path("purchase/new/", views.CreatePurchaseList.as_view(), name="add_purchase"),
    path("purhcase/<pk>/update", views.UpdatePurchaseList.as_view(), name="update_purchase"),
    path("purchase/<pk>/delete", views.DeletePurchaseList.as_view(), name="delete_purchase")
]