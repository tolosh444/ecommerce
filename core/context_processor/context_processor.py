from core.models import Settings
from core.forms import BaseContactForm


def settings(request):
    context = {
        "context_contact": BaseContactForm(),
        'settings' : Settings.objects.first(),
    }
    return context