from django import forms
from django.contrib.auth import authenticate

from .models import Account
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('example@example.com')
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': _('************')
    }))
    # Do something
    # def clean_username(self):
    #
    #     email = self.cleaned_data.get("username")
    #     if not Account.objects.filter(email=email).exists():
    #         raise forms.ValidationError("User with this email does not exist.")
    #
    #     return email

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Your first name')
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Your last name')
    }))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use. Please choose a different one.')
        return email
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