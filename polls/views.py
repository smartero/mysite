from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, EditProfile
from .models import Result, Profile
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

def index(request):
    results = Result.objects.all()
    context = {
        'results': results
    }
    return render(request, 'polls/index.html', context)

class ResultListView(ListView):
    model = Result  # what model to query
    template_name = 'polls/index.html' # looks for template at <app>/<model>_<viewtype>.html
    context_object_name = 'results' # as in def result
    #ordering = ['-time']

def register(request):
    if request.method == 'POST':    
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegisterForm()
        return render(request, 'polls/register.html', {'form': form})

class CreateOffer(CreateView):
    model = Result
    fields = ['title', 'dep', 'arr', 'pax', 'baggage', 'car', 'comment']

def logout(request):
    pass

@login_required
def profile(request):
    return render(request, 'polls/profile.html')

@login_required
def offer(request):
    pass

@login_required
def change_password(request):
    pass

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST)
        return render(request, 'polls/edit_profile.html', {'form': form})
        if form.is_valid():
            return messages.success(request, f'Changes are saved')
    else:
        form = EditProfile()
        return render(request, 'polls/edit_profile.html', {'form': form})