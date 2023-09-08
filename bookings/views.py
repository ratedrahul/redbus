from django.shortcuts import render
from django.contrib import messages
from .models import Booking, Passenger
from buses.models import Bus
from .forms import BookingForm


def book_bus(request):
    if request.method == 'POST':
        book_form = BookingForm(request.POST)
        if book_form.is_valid():
            cleaned_data = book_form.cleaned_data

            bus_id = int(cleaned_data['bus_detail'])
            passenger_name = cleaned_data['passenger_name']

            # getting bus object
            bus = Bus.objects.get(id=bus_id)

            # getting passenger object or Create a new passenger (if not exists)
            passenger, created = Passenger.objects.get_or_create(name=passenger_name)

            seat_number = cleaned_data['seat_number']
            date = cleaned_data['date']


            existing_booking = Booking.objects.filter(bus=bus, seat_number=seat_number, date=date).first()

            #confirming for existing booking
            if existing_booking:
                return render(request, 'booking_error.html', {'message': 'Seat already booked'})
            else:        
                booking = Booking(bus=bus, passenger=passenger, seat_number=seat_number, date=date)
                booking.save()
                # adding success message
                messages.success(request, "Bus Booked Successfully")

    buses = Bus.objects.all()
    book_form = BookingForm()
    return render(request, 'book_bus.html', {'buses': buses,'book_form':book_form})
