from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from core.abstact_models import AbstractBaseModel


# from .abstract_models import AbstractBaseModel
# from django.contrib.auth.hashers import make_password


# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user


class Account(AbstractUser):
    GENDERS = (
        (None, "Not chosen"),
        ("M", "Male"),
        ("F", "Female"),
    )

    username = models.CharField(_('username'), max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, null=True)
    image = models.ImageField(_('Image'), upload_to='UserImage', null=True, blank=True, default='UserImage/default.jpg')
    gender = models.TextField(
        _("Gender"),
        choices=GENDERS, null=True, blank=True
    )
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return f"Account: {self.email}"


class EmailVerification(AbstractBaseModel):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    experation = models.DateTimeField()


    def __str__(self):
        return f"Email verification for: {self.user.email}"

    def sen_verification_email(self):
        link = reverse('verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Verification link for {self.user.username}"
        message = f"To verify your account({self.user.email}), click the link below:\n\n{verification_link}"
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False

        )