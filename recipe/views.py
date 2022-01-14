from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsAuthOrReadOnly

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeChange(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
