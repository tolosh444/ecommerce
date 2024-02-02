from core.models import Settings
from core.forms import SubscribeForm


def settings(request):
    context = {
        "context_contact": SubscribeForm(),
        'settings' : Settings.objects.first(),
    }
    return context