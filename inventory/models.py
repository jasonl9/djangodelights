from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  available_quantity = models.FloatField()
  unit = models.CharField(max_length=30)
  unit_price = models.FloatField()

  def get_absolute_url(self):
    return "ingredient"

  def __str__(self):
    return self.name


class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()

  def __str__(self):
    return self.name

class RecipeRequirement(models.Model):
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField()

  def __str__(self):
    return "Recipe Requirement #" + str(self.pk) + " " + str(self.menuitem) + " - " + str(self.ingredient)

class Order(models.Model):
  timestamp = models.DateTimeField()

  def __str__(self):
    return "Order #" + str(self.pk)

class Purchase(models.Model):
  menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  order = models.ForeignKey(Order, on_delete=models.CASCADE)

  def __str__(self):
    return "Purchase #" + str(self.pk)
