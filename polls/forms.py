from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegister(UserCreationForm):
    # create additional form, in () "required" by default is True
    email = forms.EmailField()    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfile(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email']

class EditAvatar(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']