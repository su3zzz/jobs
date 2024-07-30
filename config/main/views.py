from django.shortcuts import render,redirect,get_object_or_404
import os
from main.models import CustomUser
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def choose(request):
    return render(request,'choose.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        # country = request.POST['country']
        role = request.POST['role']
        country = 'test'



        
        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.country = country
        user.role = role
        user.save()

        user = authenticate(username=email, password=password)
        if user is not None:
          
            auth_login(request,user)
            if role == 'client':
                return redirect('client')  
            else:
                return redirect('payment')  

    return render(request, 'signup.html')
    # return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(f'Username: {user.username}')
            print(f'First name: {user.first_name}')
            print(f'Last name: {user.last_name}')
            print(f'Email: {user.email}')
            print(f'Country: {user.country}')
            print(f'Role: {user.role}')
            return redirect('home')  # Change 'home' to your desired home page URL name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def worker(request):
    return render(request, 'worker.html')


def client(request):
    return render(request, 'client.html')
    

def talents(request):
    return render(request, 'talents.html')

def messages(request):
    return render(request, 'messages.html')

def workerjobs(request):
    return render(request, 'worker_jobs.html')

def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def payment(request):
    return render(request, 'payment.html')