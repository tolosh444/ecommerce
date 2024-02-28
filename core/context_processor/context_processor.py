from core.forms import SubscribeForm
from core.models import Settings


def settings(request):
    context = {
        "context_contact": SubscribeForm(),
        'settings' : Settings.objects.first(),
    }
    return context