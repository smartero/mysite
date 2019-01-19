from django.db import models
from django.utils import timezone


class Offer(models.Model):
    title = models.CharField(max_length=100)
    dep = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    pax = models.IntegerField(default=1)
    car = models.CharField(max_length=20)
    #from = models.TextField()
    #updated = models.DateTimeField(default=timezone.now) #updates on current date-time
    # on_delete - delete the ost if user is deleted
    #author = models.ForeignKey(User, on_delete=models.CASCADE)