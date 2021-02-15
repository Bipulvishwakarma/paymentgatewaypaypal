from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='confirm password (again)',
    widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class Edituserprofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']
        labels={'email':'Email'}        