from django.db import models
from cookbookapi.models.chef import Chef


class Subscription(models.Model):

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="chef")
    follower = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="following")
    created_on = models.DateField()
    deleted_on = models.DateField()
  
