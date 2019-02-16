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
    your_model = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.your_car} {self.your_model}' 

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    dep_address = models.CharField(max_length=300)
    dep_date = models.DateTimeField()
    arr_address = models.CharField(max_length=300)
    # blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage
    comment = models.CharField(max_length=200, blank=True, null=True)
    #car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    seats = models.IntegerField()
    passengers = models.ManyToManyField(Profile, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.dep_date} {self.dep_address} - {self.arr_address}, {self.seats} {self.comment}'