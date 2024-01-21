from django.urls import path, include
from .views import index, contact, base_contact

urlpatterns = [
    path('', index, name="home"),
    path('contact-us/', contact, name="contact-us"),
    path('base_contact/', base_contact, name="base-contact")
]
