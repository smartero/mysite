from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegister, EditProfile, EditAvatar, MakeOffer
from .models import Result, Profile
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

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
    return render(request, 'polls/profile.html')

@login_required
def search(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    return render(request, 'polls/search.html', context)

@login_required
def details(request, result_id):
    result = Result.objects.filter(id=result_id).first()
    return HttpResponseRedirect(request, 'polls/details/<int:>', {'result': result})

@login_required
def make_offer(request):
    if request.method == 'POST':
        form = MakeOffer(request.POST)
        form.dep = request.POST.get('dep_address')
        form.arr = request.POST.get('arr_address')
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            messages.success(request, f'Your offer has been successfully created!')
            return redirect('index')
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