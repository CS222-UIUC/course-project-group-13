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
    one = False
    two = False
    if request.method == 'POST':
        attempts = 3
        if request.POST.get("form_type") == "puzzle_one":
            clue_one_attempt = request.POST['clue_one_password']
            if (clue_one_attempt == 'vector'):
            #TODO: gives user a key
                one = True
                messages.info(request, 'Congrats you solved puzzle one')
                if (one == True & two == True):
                    messages.success(request, 'You have finished the stage, want to move on to the next one?')
            else:
                if (attempts > 0):
                    return
                else:
                    attempts = attempts - 1
        if request.POST.get("form_type") == 'puzzle_two':
            clue_two_attempt = request.POST['clue_two_password']
            if (clue_two_attempt == "This project deserves an A!"):
                two = True
                messages.info(request, 'Congrats you solved puzzle two')
                if (one == True & two == True):
                    messages.success(request, 'You have finished the stage, want to move on to the next one?')
    return render(request, 'stageone.html')

#second stage
def stagetwo(request):
    if request.method == 'POST':
        if request.POST.get('form_type') == 'puzzle_three':
            clue_three_attempt = request.POST['clue_three_passowrd']
            if (clue_three_attempt == "binary"):
                messages.info(request, "Congrats you solved puzzle three")
        if request.POST.get('form_type') == 'puzzle_four':
            clue_four_attempt = request.POST['year_puzzle']
            if (clue_four_attempt == '1998'):
                messages.info(request, 'Congrats you solved puzzle four')
        if request.POST.get('form_type') == 'puzzle_five':
            messages.info(request, 'Congrats you solved puzzle five')
    return render(request, 'stagetwo.html')

#third stage
def stagethree(request):
    if request.method == 'POST':
        if request.POST.get('form_type') == 'puzzle_six':
            clue_six_attempt = request.POST['guess_puzzle']
        if request.POST.get('form_type') == 'puzzle_seven':
            clue_seven_attempt = request.POST['clue_match']
    return render(request, 'stagethree.html')

def game_end(request):
    return render(request, 'game-end.html')