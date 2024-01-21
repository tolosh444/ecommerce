from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from order.models import Wishlist, Order

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm, BaseContactForm
from product.models import Product, Category, SubCategory

from .models import NewsLetter


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
    # wishlist_count = Wishlist.objects.filter(user=request.user).count()
    # shopping_count = Order.objects.filter(user=request.user).count()

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

def base_contact(request):

    if request.method == 'POST':
        form = BaseContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
        else:
            form = BaseContactForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def index(request):

    categories = Category.objects.all()

    sub_categories = SubCategory.objects.all()

    products = Product.objects.all().order_by("-created_at")[:8]
    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    # if request.method == "GET":
    #     form = NewsLetterForm()
    # else:
    #     form = NewsLetterForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, ("Thank you for subscribtion!"))
    #         return redirect(reverse_lazy("home"))
    #     else:
    #         messages.error(request, ("Something went wrong!!!"))
    #         return redirect(reverse_lazy("home"))

    context = {
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "page_obj": products,
        "categories": categories,
        "sub_categories": sub_categories,
        # "news_form": form,

    }
    return render(request, "home/index.html", context)




