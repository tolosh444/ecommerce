from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
# from core.models import About, Resources, Courses


from .forms import UserRegisterForm, UserProfileForm
from .models import Account

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

from django.urls import reverse


class AccountUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'account/profile.html'
    form_class = UserProfileForm
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        return context

    def get_object(self, queryset=None):

        # Get the object based on the logged-in user or any other criteria
        return get_object_or_404(Account, pk=self.kwargs['id'])

    def get_success_url(self):
        print(self.object.pk)
        # Redirect to a success URL after a successful update
        return reverse('profile', kwargs={'id': self.object.id})
