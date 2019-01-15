from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import UserCreationForm, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

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
        form = UserCreationForm()
        return render(request, 'polls/register.html', {'form': from})
    elif request.method == 'GET':
        return render(request, 'polls/register.html')

def login(request):
    return render(request, 'polls/login.html')

# logout the user, clear the session
def logout_view(request):
    logout(request)

def change_password(request):
    pass