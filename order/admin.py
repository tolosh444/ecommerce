from django.contrib import admin
from .models import Order, Wishlist, Checkout, CheckoutItem
# Register your models here.
# admin.site.register(Order)
admin.site.register(Wishlist)


@admin.register(Order)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at', ]



@admin.register(Checkout)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['get_users_first_name', 'created_at', '__str__']

    def get_users_first_name(self, obj):
        return f"{obj.user.first_name} / {obj.user.last_name}"

    get_users_first_name.short_description = 'Users Full Name'


@admin.register(CheckoutItem)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['get_users_first_name', 'product', 'created_at']

    def get_users_first_name(self, obj):
        return f"{obj.checkout.user.first_name} / {obj.checkout.user.last_name}"

    get_users_first_name.short_description = 'Users Full Name'