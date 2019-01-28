from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegister(forms.Form):
    # create additional form, in () "required" by default is True
    username = forms.CharField(label='Your name', max_length=16)
    password = forms.CharField(widget=forms.PasswordInput())
    conf = forms.CharField(label="Confirmation", widget=forms.PasswordInput())
    email = forms.EmailField()
    

class Offer(forms.ModelForm):
    pass

class EditProfile(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class EditAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']