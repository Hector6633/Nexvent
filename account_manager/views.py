from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user_data = User.objects.create_user(username=username, email=email, password=password)
            user_data.save()
            success_msg = 'Account Created'
            messages.success(request, success_msg)
            return redirect('sign_in')
        except Exception as e:
            error_msg = 'Server Error!'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')
