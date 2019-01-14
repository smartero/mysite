from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'polls/index.html')

def search(request):
    return render(request, 'polls/search.html')

def map(request):
    return render(request, 'polls/map.html')

def weather(request):
    return render(request, 'polls/weather.html')

def register(request):
    return render(request, 'polls/register.html')

def login(request):
    return render(request, 'polls/login.html')

