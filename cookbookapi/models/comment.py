from django.db import models
from cookbookapi.models.recipe import Recipe
from cookbookapi.models.chef import Chef


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)    
    content = models.CharField(max_length=500)
    created_on = models.DateField()
  
