from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstact_models import AbstractBaseModel

# Create your models here.



class ContactUs(AbstractBaseModel):
    full_name = models.CharField(
        _('Full_name'),
        max_length=20
    )
    email = models.EmailField(
        _('Email'),
        max_length=30
    )
    subject = models.CharField(
        _('Subject'),
        max_length=20
    )
    message = models.TextField(
        _('Text')
    )
    phone_number = models.CharField(
        _('Phone Num'),
        max_length=13,
    )


    class Meta:
        verbose_name = _('Contact us')
        verbose_name_plural = _('Contacts us')

    def __str__(self):
        return f"Name: {self.full_name}. Subject: {self.subject}"


class Settings(AbstractBaseModel):
    title = models.CharField(max_length=20)
    description = models.TextField()
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    facebook = models.URLField()
    youtube = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return "Site Settings"