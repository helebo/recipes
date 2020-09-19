from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('api/recipe/', views.RecipeView.as_view()), 
]
