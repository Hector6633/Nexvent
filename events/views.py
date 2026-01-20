from django.shortcuts import render
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

def event_booking(request):
    return render(request, 'event-booking-form.html')