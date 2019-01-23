from django.db import models
from django.utils import timezone

class Car(models.Model):
    your_car = models.CharField(max_length=20)
    your_model = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.your_car} {self.your_model}'

class Result(models.Model):
    title = models.CharField(max_length=100)
    dep = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    pax = models.IntegerField(default=1)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    time = timezone.now()

    def __str__(self):
        return f'{self.title}: {self.dep}, {self.to}, {self.pax} {self.car}'

