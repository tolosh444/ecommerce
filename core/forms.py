from django import forms
from django.utils.translation import gettext_lazy as _

from product.models import Subscrabed

from .models import ContactUs
from .tasks import send_mail_task


class ContactForm(forms.ModelForm):


    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'subject', 'message', 'phone_number']



class SubscribeForm(forms.ModelForm):
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
    def send_email(self):
        send_mail_task.apply_async(args=[
    self.cleaned_data["email"], self.cleaned_data["name"]
    ]
)

    class Meta:
        model = Subscrabed
        fields = ('name', 'email',)


