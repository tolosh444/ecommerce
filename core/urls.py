from django.urls import path, include
from .views import index, contact, subscribe_success

urlpatterns = [
    path('', index, name="home"),
    path('contact-us/', contact, name="contact-us"),
    path('subscribe/', subscribe_success, name="subscribe")
]
