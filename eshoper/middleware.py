from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if user is authenticated and trying to access the login page
        if request.user.is_authenticated and request.path == reverse('login'):
            return redirect('home')  # Redirect to the home page or any other page

        return response