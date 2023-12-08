from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("ingredient/", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredient/<pk>/delete", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path("menuitem/", views.MenuItemList.as_view(), name="menuitemlist"),
    path("purchase/", views.PurchaseList.as_view(), name='purchaselist')
]