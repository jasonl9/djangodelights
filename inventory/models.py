from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  avaliable_quantity = models.IntegerField
  unit = models.CharField(max_length=30)
  unit_price = models.FloatField


class MenuItem(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField

class RecipeRequirement(models.Model):
  pass

class Order(models.Model):
  timestamp = models.DateTimeField

class Purchase(models.Model):
  pass
