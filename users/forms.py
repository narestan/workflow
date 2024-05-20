# myapp/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100,
                               widget=forms.TextInput(attrs={'class': 'mt-1 block w-full'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'mt-1 block w-full'}))