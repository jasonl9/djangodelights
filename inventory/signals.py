from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase, RecipeRequirement

#update inventory quantity after a purchase
@receiver(post_save, sender=Purchase)
def goods_sold(sender, instance, created, **kwargs):
    if created:
        menu_item = instance.menu_item
        recipes = RecipeRequirement.objects.filter(menu_item=menu_item.pk)
        for recipe in recipes:
            recipe.ingredient.quantity -= recipe.quantity
            recipe.ingredient.save()