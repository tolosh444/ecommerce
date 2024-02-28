from django.contrib.auth import views as auth_views
from django.urls import path

from .views import AccountRegistrationView, AccountUpdateView, UserVerificationView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/index.html'), name='logout'),
    path('register/', AccountRegistrationView.as_view(), name='register'),
    path('profile/<int:id>/', AccountUpdateView.as_view(), name='profile'),
    path('verification/<str:email>/<uuid:code>/', UserVerificationView.as_view(), name='verification'),


]
