from django.db import models
from django.contrib.auth.models import User


class Chef(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, default=None)
    created_on = models.DateField()
    active = models.CharField(max_length=50)
    subscriptions = models.ManyToManyField(User, related_name="subscribers" )
    
    
    @property
    def subscribed(self):
        return self.__subscribed

    @subscribed.setter
    def subscribed(self, value):
        self.__subscribed = value

