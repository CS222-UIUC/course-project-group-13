from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    points = models.CharField(max_length=10)
    #TODO: create an inventory for the user
    def __str__(self):
        return self.username

    def getPoints(self):
        return self.points