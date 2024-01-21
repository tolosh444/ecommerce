from django import forms
from .models import ContactUs, NewsLetter
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):


    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message', 'phone_number']


class BaseContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': "text",
        'id': "name",
        'required': "required",
        'placeholder': 'Your Name...',
        'style': 'opacity: 0.8;'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': "email",
        'id': "email",
        'required': "required",
        'placeholder': 'Your Email...',
        'style': 'opacity: 0.8;'
    }))

    class Meta:
        model = NewsLetter
        fields = ('name', 'email',)


