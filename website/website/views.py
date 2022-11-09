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

def game_begin(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not logged in')
        return redirect('login')
    return render(request, 'game-begin.html')

#first stage
def stageone(request):
    if request.method == 'POST':
        clue_one_attempt = request.POST['clue_one_password']
        if (clue_one_attempt == 'vector'):
            #TODO: gives user a key
            messages.info(request, 'Congrats')
        else:
            if (attempts > 0):
                return
            else:
                attempts = attempts - 1
    return render(request, 'stageone.html')

#second stage
def stagetwo(request):
    return render(request, 'stagetwo.html')

#third stage
def stagethree(request):
    return render(request, 'stagethree.html')

def game_end(request):
    return render(request, 'game-end.html')