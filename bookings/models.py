from django.db import models
from buses.models import Bus

class Passenger(models.Model):
    name = models.CharField(max_length=100)

class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    date = models.DateField()
