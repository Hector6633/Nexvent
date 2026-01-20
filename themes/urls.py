from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('sign-up', sign_up, name='sign_up'),
    path('sign-in', sign_in, name='sign_in'),
    path('success', success, name='success'),
    path('error', error, name='error'),
]
