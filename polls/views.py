from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegister, EditProfile, EditAvatar
from .models import Result, Profile
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

def index(request):
    return render(request, 'polls/index.html')

def register(request):
    if request.method == 'POST':    
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in.')
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
    return render(request, 'polls/rearch.html', context)

class ResultListView(ListView):
    model = Result  # what model to query
    template_name = 'polls/search.html' # looks for template at <app>/<model>_<viewtype>.html
    context_object_name = 'results' # as in def result
    #ordering = ['-time']


@login_required
def make_offer(request):
    pass



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