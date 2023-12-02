from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  available_quantity = models.FloatField()
  unit = models.CharField(max_length=30)
  unit_price = models.FloatField()


class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()

class RecipeRequirement(models.Model):
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField()

class Order(models.Model):
  timestamp = models.DateTimeField()

class Purchase(models.Model):
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
