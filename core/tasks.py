from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_task():
    from product.models import Subscrabed
    subscrabed = Subscrabed.objects.all()
    print("Mail sending.......")
    subject = 'Welcome to Eshopper.com'
    message = 'Hi, thank you for using our service'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in subscrabed]
    send_mail(subject, message, email_from, recipient_list)
    return "Mail has been sent........"
