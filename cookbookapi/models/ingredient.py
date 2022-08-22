from django.db import models

class Ingredient(models.Model):
    element = models.CharField(max_length=50)