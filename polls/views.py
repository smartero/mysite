from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import UserRegisterForm

def index(request):
    return render(request, 'polls/index.html')

@login_required
def offer(request):
    return render(request, 'polls/offer.html')

def map(request):
    return render(request, 'polls/map.html')

def weather(request):
    return render(request, 'polls/weather.html')

def register(request):
    if request.method == 'POST':    
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'polls/register.html', {'form': form})

@login_required
def change_password(request):
    pass