from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Result


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

TRIP_CHOICES = (
    ('oneway', 'Oneway'),
    ('roundrip', 'Roundrip'),
)
 
class MakeOffer(forms.ModelForm):
    pax = forms.IntegerField(label='Passengers', min_value=1, max_value=5)
    #trip_type = forms.ChoiceField(widget=forms.RadioSelect, choices=TRIP_CHOICES,)
    comment = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Result
        fields = ['title', 'pax', 'comment']