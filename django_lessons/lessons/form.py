from django import forms
from django.contrib.auth.models import User
from .models import user_profile

class user_form(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password') 
