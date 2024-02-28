from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.translation import gettext_lazy as _


from .models import Account
from .tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('example@example.com')
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': _('************')
    }))


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
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Your username')
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
        fields = ['first_name', 'last_name', 'gender', 'email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'readonly': True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'readonly': True
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file'
    }))

    gender = forms.RadioSelect()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'image', 'gender', 'email']