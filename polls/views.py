from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Result

def index(request):
    return render(request, 'polls/index.html')

def register(request):
    if request.method == 'POST':    
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def result(request):
    context = {
        'results': Result.objects.all()
    }
    return render(request, 'polls/results.html', context)

def offer(request):
    pass 
    
def offer_details(request, offer_id):
    try:
        offer = Result.objects.get(pk=offer_id)
    except Result.DoesNotExist:
        raise Http404('Offer doesn\'t exist')
    context = {
        'result': result
    }
    return render(request, 'polls/offer_details.html', context)

def map(request):
    return render(request, 'polls/map.html')

@login_required
def change_password(request):
    pass