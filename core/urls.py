from django.urls import include, path

from .views import contact, index, subscribe_success

urlpatterns = [
    path('', index, name="home"),
    path('contact-us/', contact, name="contact-us"),
    path('subscribe/', subscribe_success, name="subscribe")
]
