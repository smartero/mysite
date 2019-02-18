from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Result
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field, HTML, MultiField

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
    seats = forms.IntegerField(label='Seats', min_value=1, max_value=4, initial=1)
    #trip_type = forms.ChoiceField(widget=forms.RadioSelect, choices=TRIP_CHOICES,)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}), required=False)
    class Meta:
        model = Result
        fields = '__all__'
    # customizing crispy form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Fieldset(
                    '',
                        Field('title', id='title'),
                        Field('dep_address', css_class='form-group'),
                        Field('arr_address', css_class='form-group'),
                        Div(
                            Div('dep_date', css_class='form-group col'),
                            Div('seats', css_class='form-group col-md-auto'),
                            css_class='form-row'),
                        Field('comment', css_class='form-group', css_rows='3')
            )
        )
        
        super(MakeOffer,self).__init__(*args, **kwargs)