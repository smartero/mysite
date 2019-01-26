from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # create additional form, in () "required" by default is True
    email = forms.EmailField()

    class Meta:
        # when the form is valid it influences a model User
        model = User
        # the fields to be shown
        fields = ['username', 'email', 'password1', 'password2']
