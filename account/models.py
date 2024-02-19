from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    def __str__(self):
        return f"Account: {self.email}"
