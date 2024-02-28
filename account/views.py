from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import UserProfileForm, UserRegisterForm
from .models import Account, EmailVerification

User = get_user_model()


class AccountRegistrationView(SuccessMessageMixin, generic.CreateView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    model = User
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully!'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)




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


class UserVerificationView(TemplateView):
    template_name = 'account/verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = get_object_or_404(User, email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)

        if email_verification.exists():
            user.is_verified = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))
    def get_context_data(self, *args, **kwargs):
        # Your additional context logic here
        return super().get_context_data(*args, **kwargs)
