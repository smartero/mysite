from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page - here 
        else:
            message.error(request, 'Invalid login')
    else:
        return render(request, 'polls/login.html')

@login_required
def change_password(request):
    pass