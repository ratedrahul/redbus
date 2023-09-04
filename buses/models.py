# Create your models here.
from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    stops = models.ManyToManyField('Stop')

class Stop(models.Model):
    name = models.CharField(max_length=100)

class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
