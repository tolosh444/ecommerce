
import uuid
from celery import shared_task
from .models import Account, EmailVerification
from datetime import timedelta
from django.utils.timezone import now

@shared_task
def send_email_verification(user_id):
    print(f"Sending email verification for user {user_id}")
    user = Account.objects.get(id=user_id)
    experation = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, experation=experation)
    record.sen_verification_email()