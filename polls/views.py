from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Offer

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


def offer(request):
    context = {
        'offers': Offer.objects.all()
    }
    return render(request, 'polls/offer.html', context)

def offer_details(request, offer_id):
    try:
        offer = Offer.objects.get(pk=offer_id)
    except Offer.DoesNotExist:
        raise Http404('Offer doesn\'t exist')
    context = {
        'offer': offer
    }
    return render(request, 'polls/offer_details.html', context)

def map(request):
    return render(request, 'polls/map.html')

def weather(request):
    return render(request, 'polls/weather.html')


@login_required
def change_password(request):
    pass