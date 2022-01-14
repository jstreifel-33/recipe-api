from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeList.as_view(), name='recipe_list'),
    path('<int:pk>', RecipeChange.as_view(), name='recipe_change'),
]