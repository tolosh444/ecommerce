from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from product.models import Product, Category, SubCategory

from .models import Wishlist, Order, Checkout, CheckoutItem
from core.choices import STATUS_CHOICES
import random

# Create your views here.

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    wishlist, created = Wishlist.objects.get_or_create(user=user, product=product)

    if created:
        messages.success(request, "Product added to wishlist.")
    else:
        messages.error(request, "Product already exists in wishlist.")

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required
def delete_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    try:
        wishlist = Wishlist.objects.get(user=user, product=product)
        wishlist.delete()


        messages.success(request, "Product deleted from wishlist.")
    except Wishlist.DoesNotExist:
        messages.error(request, "Something went wrong.")

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def users_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    shopping_count = Order.objects.filter(user=request.user).count()

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "categories": categories,
        "sub_categories": sub_categories,
    }
    return render(request, 'user/wishlist.html', context)


@login_required
def users_shopping_cart(request):
    shopping_cart_items = Order.objects.filter(user=request.user, status="BASKET")
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    shopping_count = Order.objects.filter(user=request.user).count()

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()


    total_price = 0
    for item in shopping_cart_items:
        total_price = total_price + (item.product_qty * item.product.selling_price)

    grand_total = total_price + 10

    context = {
        "shopping_cart_items": shopping_cart_items,
        "shopping_count": shopping_count,
        "wishlist_count": wishlist_count,
        "categories": categories,
        "sub_categories": sub_categories,
        "total_price": total_price,
        "grand_total": grand_total
    }
    return render(request, 'user/shopping_cart.html', context)

@login_required
def add_to_shopping_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    try:
        order = Order.objects.get(user=user, product=product)
        messages.error(request, "Product already exists in the shopping cart.")
    except Order.DoesNotExist:
        order = Order(user=user, product=product, status=STATUS_CHOICES[0][0], product_qty=1)
        order.save()
        messages.success(request, "Product added to the shopping cart.")

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def delete_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    try:
        order = Order.objects.get(user=user, product=product)
        order.delete()

        messages.success(request, "Product deleted from cart.")
    except Order.DoesNotExist:
        messages.error(request, "Something went wrong.")

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def save_data(request):
    if request.method == "POST" and request.is_ajax():
        data = request.POST.getlist('data[]')
        # Process the data and save it to the database
        # For example, you can create a model instance and save the data
        # Here, we'll just return a success response for demonstration purposes.
        return JsonResponse({'message': 'Data saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def checkout_order(request):
    # Coounters wor Wishlist and Shopping cart
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    shopping_count = Order.objects.filter(user=request.user).count()

    rawcart = Order.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Order.objects.get(id=item.id).delete()


    cart_items = Order.objects.filter(user=request.user)
    total_price = 0
    for item in cart_items:
        total_price = total_price + (item.product_qty * item.product.selling_price)
    grand_total = total_price + 10
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "shopping_count": shopping_count,
        "wishlist_count": wishlist_count,
        "grand_total": grand_total,

    }
    return render(request, "user/checkout.html", context)


@login_required
def place_order(request):
    if request.method == "POST":
        neworder = Checkout()
        neworder.user = request.user
        neworder.first_name = request.POST.get('first_name')
        neworder.last_name = request.POST.get('last_name')
        neworder.email = request.POST.get('email')
        neworder.phone_number = request.POST.get('phone_number')
        neworder.address1 = request.POST.get('address1')
        neworder.address2 = request.POST.get('address2')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.zip_code = request.POST.get('zip_code')


        # neworder.payment_mode = request.POST.get('payment_mode')
        # neworder.payment_id = request.POST.get('payment_id')

        order = Order.objects.filter(user=request.user)
        order_total_price = sum(item.product.selling_price * item.product_qty for item in order)


        neworder.total_price = order_total_price

        trackno = f'ecommerce{random.randint(1111111, 9999999)}'
        while Checkout.objects.filter(tracking_no=trackno) is None:
            trackno = f'ecommerce{random.randint(1111111, 9999999)}'

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Order.objects.filter(user=request.user)
        for item in neworderitems:
            CheckoutItem.objects.create(
                checkout=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
                size=item.product.size,
                color=item.product.color
            )

            # To decrease the product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()
        # To clear user's Order
        Order.objects.filter(user=request.user).delete()

        # order_del = Order.objects.filter(user=request.user)
        # for order in order_del:
        #     order.status = "DONE"
        #     order.save()
        messages.success(request, "Your product has been placed successfully")


    context = {
        "order_total_price": order_total_price,
    }

    return redirect('/')