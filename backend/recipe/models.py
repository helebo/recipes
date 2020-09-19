from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    food_type = models.CharField(max_length=40)
    

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    time = models.IntegerField()
    instruction = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(Ingredient)