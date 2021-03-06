from django.shortcuts import render

from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



