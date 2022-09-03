from django.db import models
from cookbookapi.models.recipe import Recipe
from cookbookapi.models.measure import Measure


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=50)    
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
  