from django.contrib.auth import get_user_model
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

# from core.models import About, Resources, Courses


from .forms import UserRegisterForm



User = get_user_model()


class AccountRegistrationView(generic.CreateView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AccountUpdateView(generic.UpdateView):
    template_name = 'account/register.html'

    model = User
    success_url = reverse_lazy('home')


