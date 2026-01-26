from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user
from django.contrib import messages
# Create your views here.
@unauthenticated_user
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
            error_msg = 'Username is already exist'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

@unauthenticated_user
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            error_msg = 'Invalid User'
            messages.error(request, error_msg)
            return redirect('sign_in')
    return render(request, 'sign-in.html')

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    success_msg = 'Sign Out Successfully'
    messages.success(request, success_msg)
    return redirect('sign_in')
