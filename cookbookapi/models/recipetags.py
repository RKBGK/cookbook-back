from django.db import models
from cookbookapi.models.chef import Chef

from cookbookapi.models.recipe import Recipe
from cookbookapi.models.tag import Tag

class RecipeTag(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) 
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE) 