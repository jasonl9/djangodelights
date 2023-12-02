from django.urls import path

from . import views

urlpatterns = [
    path("ingredient/", views.IngredientList.as_view(), name="ingredientlist")
]