from django.urls import path

from . import views

urlpatterns = [
    path("ingredient/", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/<pk>/delete", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path("menuitem/", views.MenuItemList.as_view(), name="menuitemlist"),
]