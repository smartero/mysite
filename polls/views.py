from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Result, Profile
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

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
            return redirect('index')
    else:
        form = UserRegisterForm()
        return render(request, 'polls/register.html', {'form': form})

class CreateOffer(CreateView):
    model = Result
    fields = ['title', 'dep', 'arr', 'pax', 'baggage', 'car', 'comment']

@login_required
def profile(request):
    return render(request, 'polls/profile.html')

def offer(request):
    pass

@login_required
def change_password(request):
    pass