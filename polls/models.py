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
    car_model = models.CharField(max_length=20)
    car_color = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.car_model} {self.car_color}' 

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, help_text='Say a coule of words to attract attention')
    dep_address = models.CharField(max_length=300, help_text='City or district')
    dep_date = models.DateField()
    arr_address = models.CharField(max_length=300, help_text='City or district')
    # blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage
    comment = models.CharField(max_length=200, blank=True, null=True)
    #car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    seats = models.IntegerField()
    passengers = models.ManyToManyField(Profile, blank=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.title} {self.dep_date} {self.dep_address} - {self.arr_address}, {self.seats} {self.comment}'