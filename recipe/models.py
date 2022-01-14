from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    servings = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
