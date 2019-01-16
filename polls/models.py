from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Resorts(models.Model):
    name = models.CharField(max_length=100)
    adress = models.TextField()
    updated = models.DateTimeField(default=timezone.now) #updates on current date-time
    # on_delete - delete the ost if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)