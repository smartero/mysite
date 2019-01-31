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

class TripType(models.Model):
    ONEWAY = 'OW'
    ROUNDTRIP = 'RT'
    TRIP_CHOICES = (
        (ONEWAY, 'Oneway'),
        (ROUNDTRIP, 'Roundtrip'),
    )
    choices = models.CharField(choices=TRIP_CHOICES, default=ONEWAY, max_length=2)
    your_choice = models.CharField(max_length=50)

class Result(models.Model):
    
    title = models.CharField(max_length=100)
    #trip_type = models.ForeignKey(TripType, blank=False, on_delete=models.CASCADE)
    dep_city = models.CharField(max_length=100)
    #dep_date = models.DateField(default=date.today)
    resort = models.CharField(max_length=100)
    pax = models.IntegerField(default=1)
    baggage = models.IntegerField(default=0)
    boots = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    comment = models.TextField(max_length=300, default=None)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.dep_city}, {self.resort}, {self.pax} {self.car}'