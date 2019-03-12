from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    UserRegister, EditProfile, EditAvatar, 
    MakeOffer, )
from .models import Result, Profile
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

def index(request):
    if request.method == 'POST':
        messages.info(request, f'Please login')
        return redirect('login')
    return render(request, 'polls/index.html')

def register(request):
    if request.method == 'POST':    
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            u = User.objects.filter(username=username).last()
            profile = Profile.objects.create(user=u)
            profile.save()
            messages.success(request, f'Account created for {username}! You can log in now')
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'polls/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    driver = Result.objects.filter(user=user)
    passenger = Result.objects.filter(passengers=Profile.objects.filter(user=user).first())
    context = {
        'driver': driver,
        'passenger': passenger
    }
    return render(request, 'polls/profile.html', context)

@login_required
def search(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    return render(request, 'polls/search.html', context)

class SearchListView(ListView):
    model = Result
    template_name = 'polls/search.html'
    context_object_name = 'results'

@login_required
def details(request, pk):
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, f'Successfully reserved')
            return redirect('profile')
    else:
        details = Result.objects.get(pk=pk)
        context = {
            'details': details
        }
    return render(request, 'polls/details.html', context)

@login_required
def make_offer(request):
    if request.method == 'POST':
        form = MakeOffer(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            messages.success(request, f'Your offer has been successfully created!')
            return redirect('search')
    else:
        form = MakeOffer()
    return render(request, 'polls/make_offer.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = EditProfile(request.POST)
        a_form = EditAvatar(request.POST)
        context = {
        'p_form': p_form,
        'a_form': a_form
        }
        messages.success(request, f'Changes are saved')
        return redirect('profile')
    else:
        p_form = EditProfile()
        a_form = EditAvatar()
        context = {
            'p_form': p_form,
            'a_form': a_form
        }
        return render(request, 'polls/edit_profile.html', context)