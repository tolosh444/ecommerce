from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (add_to_shopping_cart, add_to_wishlist, checkout_order,
                    delete_from_cart, delete_from_wishlist, place_order,
                    save_data, users_shopping_cart, users_wishlist)

urlpatterns = [
    # wishlist
    path("wishlist", users_wishlist, name="wishlist"),
    path("wishlist/add-to-wishlist/<int:product_id>", add_to_wishlist, name="user-wishlist"),
    path("wishlist/delete-from-wishlist/<int:product_id>", delete_from_wishlist, name="delete-from-wishlist"),
    # order
    path("shopping-cart", users_shopping_cart, name="shopping-cart"),
    path("shopping-cart/add-to-shopping-cart/<int:product_id>", add_to_shopping_cart, name="user-shopping-cart"),
    path("shopping-cart/delete-from-cart/<int:product_id>", delete_from_cart, name="delete-from-cart"),
    path("shopping-cart/checkout", checkout_order, name="checkout-order"),
    path("shopping-cart/checkout/place-order", place_order, name="place-order"),
    path('save_data/', save_data, name='save_data'),

          ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)