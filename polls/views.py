from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'polls/index.html')

@login_required
def search(request):
    return render(request, 'polls/search.html')

def map(request):
    return render(request, 'polls/map.html')

def weather(request):
    return render(request, 'polls/weather.html')

def register(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form': form})

def login(request):
    return render(request, 'polls/login.html')



def change_password(request):
    pass