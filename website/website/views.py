from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.contrib import messages

#homepage
def homepage(request):
    return render(request, 'homepage.html')

#registration page for user
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already in use')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('login')
        
    return render(request, 'register.html')

#login page for user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Either the username or password is invalid')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def game_begin(request):
    if request.method == 'POST': 
        if not request.user.is_authenticated:
            messages.info(request, 'You are not logged in')
            return redirect('login')
        else:
            return redirect('http://127.0.0.1:8000/stageone')
    return render(request, 'game-begin.html')

#first stage
def stageone(request):
    return render(request, 'stageone.html')

#second stage
def stagetwo(request):
    return render(request, 'stagetwo.html')

#third stage
def stagethree(request):
    return render(request, 'stagethree.html')

def game_end(request):
    return render(request, 'game-end.html')