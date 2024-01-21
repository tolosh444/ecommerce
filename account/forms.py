from django import forms
from .models import Account
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Your first name')
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Your last name')
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': _('youremail@example.com')
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*********'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '*********'
    }))
    gender = forms.RadioSelect()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'gender', 'email', 'password1', 'password2']