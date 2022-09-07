from unicodedata import category
from django.db import models
from cookbookapi.models.chef import Chef
from cookbookapi.models.category import Category

class Recipe(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=500, default=None)
    description = models.CharField(max_length=50)
    video_url = models.URLField(max_length=500, default=None)
    recipe = models.CharField(max_length=500, default=None)
    cookingtime = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="recipetype") 
    favorite = models.ManyToManyField(Chef, related_name="userfav") 
    
    @property
    def categorized(self):
        return self.__categorized

    @categorized.setter
    def categorized(self, value):
        self.__categorized = value
        
    def __str__(self):
        return self.title
        
