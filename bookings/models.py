from django.db import models
from buses.models import Bus

class Passenger(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"Booking for seat {self.seat_number} on {self.date} for passenger {self.passenger.name} on bus {self.bus.name}"


