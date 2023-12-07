from django.db import models
from datetime import datetime

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  quantity = models.FloatField()
  unit = models.CharField(max_length=30)
  unit_price = models.FloatField()

  def get_absolute_url(self):
    return "ingredient"

  def __str__(self):
    return self.name


class MenuItem(models.Model):
  title = models.CharField(max_length=100)
  price = models.FloatField()

  def __str__(self):
    return self.title

class RecipeRequirement(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField()

  def __str__(self):
    return "Recipe Requirement #" + str(self.pk) + " " + str(self.menu_item) + " - " + str(self.ingredient)

class Purchase(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(default=datetime.now)

  def __str__(self):
    return "Purchase #" + str(self.pk)