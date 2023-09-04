from django.shortcuts import render
from .models import Bus

def homepage(request):
    return render(request,'homepage.html')


def list_buses(request):
    buses = Bus.objects.all()
    return render(request, 'list_buses.html', {'buses': buses,'welcome':'Welcome Rahul bro'})
