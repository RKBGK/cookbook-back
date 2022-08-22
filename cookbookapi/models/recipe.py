from django.db import models
from cookbookapi.models.chef import Chef

class Recipe(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=500, default=None)
    description = models.CharField(max_length=50)
    video_url = models.URLField(max_length=500, default=None)
    recipe = models.CharField(max_length=500, default=None)
    cooktime = models.IntegerField()