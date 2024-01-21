from django import forms

from product.models import ProductReviews


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': "text",
        'id': "review",
        'required': "required",
        'placeholder': 'Your review...',
        'style': 'opacity: 0.8;'
    }))
    rating = forms.RadioSelect()


    class Meta:
        model = ProductReviews
        fields = ("review", "rating",)
        widgets = {'product': forms.HiddenInput()}