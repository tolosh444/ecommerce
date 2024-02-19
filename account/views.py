from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
# from core.models import About, Resources, Courses
from django.urls import reverse

from .forms import UserRegisterForm, UserProfileForm
from .models import Account

User = get_user_model()


class AccountRegistrationView(generic.CreateView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully!'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



@login_required
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
        return get_object_or_404(Account, id=self.kwargs['id'])

    def get_success_url(self):
        print(self.object.pk)
        # Redirect to a success URL after a successful update
        return reverse('profile', kwargs={'id': self.object.id})
