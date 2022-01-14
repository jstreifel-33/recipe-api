from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Recipe

class RecipeModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_recipe = Recipe.objects.create(
            name = 'Name of Recipe',
            author = test_user,
            servings = 3,
            ingredients = 'test ingredients',
            instructions = 'test instructions',
        )
        test_recipe.save()

    def test_blog_content(self):
        recipe = Recipe.objects.get(id=1)

        self.assertEqual(str(recipe.author), 'tester')
        self.assertEqual(recipe.name, 'Name of Recipe')
        self.assertEqual(recipe.servings, 3)
        self.assertEqual(recipe.ingredients, 'test ingredients')
        self.assertEqual(recipe.instructions, 'test instructions')
