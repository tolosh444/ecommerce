from django import forms
from django.utils.translation import gettext_lazy as _

from core.choices import SIZE_CHOICE

from .models import Order


class OrderForm(forms.ModelForm):
    size = forms.ChoiceField(
        choices=SIZE_CHOICE,
        widget=forms.RadioSelect(attrs={
            'class': 'form-control',

        })
    )
    class Meta:
        model = Order
        fields = ("product", "status", "size", "color",)