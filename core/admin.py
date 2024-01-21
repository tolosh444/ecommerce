from django.contrib import admin
from .models import ContactUs, Settings, NewsLetter
# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Settings)
admin.site.register(NewsLetter)
