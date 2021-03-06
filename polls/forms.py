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

class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class AvatarUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
 
class MakeOffer(forms.ModelForm):
    seats = forms.IntegerField(label='Seats', min_value=1, max_value=7, initial=1, help_text='Free seats available for reservation')
    #trip_type = forms.ChoiceField(widget=forms.RadioSelect, choices=TRIP_CHOICES,)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}), required=False, help_text='Any additional info that you consider important')
    
    class Meta:
        model = Result
        fields = '__all__'