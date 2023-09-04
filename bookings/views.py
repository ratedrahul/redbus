from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Booking, Passenger
from buses.models import Bus

def book_bus(request):
    buses = Bus.objects.all()
    return render(request, 'book_bus.html', {'buses': buses})
