from django.shortcuts import render, redirect
from . models import *
# Create your views here.

def events(request):
    events = {
        'events': Event_Company.objects.all()
    }
    return render(request, 'events.html', events)

def readmore(request, pk):
    event_details = {
        'event_detail': Event_Company.objects.get(id=pk)
    }
    return render(request, 'readmore.html', event_details)

def selected_event(request, pk):
    event = {
        'event':Event_Company.objects.get(pk=pk)
    }
    return render(request, 'event-booking-form.html', event)

def event_booking(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['number']
            event_company_name = request.POST['event_company_name']
            event_type = request.POST['event_type']
            event_price = request.POST['event_price']
            event_location = request.POST['event_location']
            event_booking_date = request.POST['date']
            booking_data = Event_Booking.objects.create(name=name, email=email, number=number, event_company_name=event_company_name,
                                                        event_type=event_type, event_price=event_price, event_location=event_location,
                                                        event_booking_date=event_booking_date)
            booking_data.save()
            return redirect('success')
        except Exception as e:
            return redirect('error')
    return render(request, 'event-booking-form.html')