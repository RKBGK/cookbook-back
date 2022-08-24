from django.db import models
from cookbookapi.models.recipe import Recipe
from cookbookapi.models.ingredient import Ingredient
from cookbookapi.models.measure import Measure


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)    
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
  