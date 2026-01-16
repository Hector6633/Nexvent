from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def events(request):
    return render(request, 'events.html')

def readmore(request):
    return render(request, 'readmore.html')

def event_booking(request):
    return render(request, 'event-booking-form.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')
