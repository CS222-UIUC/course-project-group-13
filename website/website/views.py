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

def stagone(request):
    if request.method == 'POST':
        clue_one_attempt = request.POST['clue_one_password']
        if (clue_one_attempt == 'vector'):
            messages.info(request, 'Congrats')
        else:
            if (attempts > 0):
                return
            else:
                attempts = attempts - 1
    return render(request, 'stageone.html')