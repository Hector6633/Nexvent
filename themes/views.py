from django.shortcuts import render, redirect
from . models import Feedback
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['number']
            message = request.POST['message']
            feedback_data = Feedback.objects.create(name=name, email=email, number=number, message=message)
            feedback_data.save()
            success_msg = "Thank you for your Feedback"
            messages.success(request, success_msg)
            return redirect('feedback')
        except Exception as e:
            error_msg = 'Server updating'
            messages.error(request, error_msg)
            return redirect('feedback')
    return render(request, 'feedback.html')

def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')
