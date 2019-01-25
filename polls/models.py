from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='/avatar_pics/default.jpg', upload_to='avatar_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Car(models.Model):
    your_car = models.CharField(max_length=20)
    your_model = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.your_car} {self.your_model}'

class Result(models.Model):
    title = models.CharField(max_length=100)
    dep = models.CharField(max_length=100)
    #date
    arr = models.CharField(max_length=100)
    pax = models.IntegerField(default=1)
    baggage = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    comment = models.TextField(max_length=300, default=None)
    time = timezone.now()

    def __str__(self):
        return f'{self.title}: {self.dep}, {self.arr}, {self.pax} {self.car}'

