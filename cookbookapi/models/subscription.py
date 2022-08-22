from django.db import models
from cookbookapi.models.chef import Chef


class Subscription(models.Model):

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="Chef")
    follower = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="following")
    created_on = models.DateField()
    deleted_on = models.DateField()
  
    @property
    def subscribed(self):
        return self.__subscribed

    @subscribed.setter
    def subscribed(self, value):
        self.__subscribed = value
