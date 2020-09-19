from rest_framework import serializers
from .models import Recipe, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'time', 'instruction')

