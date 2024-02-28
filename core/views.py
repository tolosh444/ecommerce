import smtplib
from email.message import EmailMessage

from celery import shared_task
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
#email
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from order.models import Order, Wishlist
from product.models import Category, Product, SubCategory, Subscrabed

from .forms import ContactForm, SubscribeForm

# Create your views here.

def contact(request):


    if request.user and not isinstance(request.user, AnonymousUser):
        user_id = request.user.id
        wishlist_count = Wishlist.objects.filter(user_id=user_id).count()
        shopping_count = Order.objects.filter(user_id=request.user).count()
    else:
        # Handle the case where the user is anonymous or request.user is not available
        wishlist_count = 0
        shopping_count = 0

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    current_url = reverse_lazy("contact-us")

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Thank you for contacting us! We will be in touch shortly."))
            return HttpResponseRedirect(current_url)
        else:
            messages.error(request, ("Something went wrong!!!"))
            return HttpResponseRedirect(current_url)


    context = {
        'form': form,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "categories": categories,
        "sub_categories": sub_categories,
    }
    return render(request, 'contact/contact.html', context)

# def base_contact(request):
#
#     if request.method == 'POST':
#         form = BaseContactForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('home'))
#         else:
#             form = BaseContactForm()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def subscribe_success(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        if not Subscrabed.objects.filter(email=email).exists():
            Subscrabed.objects.create(email=email, name=name)
            messages.success(request, _("Congratulations! You have successfully subscribed."))
            send_mail(
                subject="Thank you for subscribing!",
                message=f"{name}! Welcome to E-commerce!",
                from_email="talishaqil@yandex.com",
                recipient_list=[email]
            )
            return redirect(reverse_lazy('home'))
        else:
            messages.error(request, _("You have already subscribed!"))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))









def index(request):

    categories = Category.objects.all()

    sub_categories = SubCategory.objects.all()

    products = Product.objects.all().order_by("-created_at")[:8]
    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()



    context = {
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "page_obj": products,
        "categories": categories,
        "sub_categories": sub_categories,
        # "news_form": form,

    }
    return render(request, "home/index.html", context)




