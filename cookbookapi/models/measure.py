from django.db import models

class Measure(models.Model):
    unit = models.CharField(max_length=50)
            
    def __str__(self):
        return self.unit