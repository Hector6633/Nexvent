from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('events', events, name='events'),
    path('readmore', readmore, name='readmore'),
    path('event-booking-form', event_booking, name='event_booking'),
    path('sign-up', sign_up, name='sign_up'),
    path('sign-in', sign_in, name='sign_in'),
]
