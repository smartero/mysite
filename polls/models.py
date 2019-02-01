from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import DateTimeField

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
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dep_adress} - {self.arr_adress}, {self.pax}, {self.car}, {self.comment}'