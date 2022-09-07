from django.db import models
from cookbookapi.models.recipe import Recipe
from cookbookapi.models.measure import Measure


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='element')
    ingredient = models.CharField(max_length=50)    
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name='measureunit')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
            
    def __str__(self):
        return self.ingredient 
    
  