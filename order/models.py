from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstact_models import AbstractBaseModel
from core.choices import (COLOR_CHOICES, COUNTRY_CHOICES, SIZE_CHOICE,
                          STATUS_CHOICES)


class Order(AbstractBaseModel):
    user = models.ForeignKey(
        "account.Account",
        on_delete=models.CASCADE,
        null=True)

    # manytomany elemek lazimdir`
    # product = models.OneToOneField(
    #     "product.Product",
    #     on_delete=models.CASCADE,
    #     related_name="order_product",
    # )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="order_product",
    )


    product_qty = models.PositiveIntegerField(
        null=False,
        blank=False)

    status = models.CharField(
        _("Status"),
        choices=STATUS_CHOICES,
        max_length=10,
        default="BASKET"
    )

    size = models.CharField(
        _('Size'),
        choices=SIZE_CHOICE,
        max_length=10,
        null=True,)

    color = models.CharField(
        _('Color'),
        max_length=20 ,
        choices=COLOR_CHOICES,
        null=True)


    class Meta:
        verbose_name = 'Basket item'
        verbose_name_plural = 'Basket items'

    def __str__(self):
        return f"{self.user.email}'s Orderlist"
    @property
    def total_price(self):
        return self.product.selling_price * self.product_qty

class Wishlist(AbstractBaseModel):
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}'s Wishlist"

class Checkout(AbstractBaseModel):
    user = models.ForeignKey(
        "account.Account",
        on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone_number = models.CharField(max_length=150, null=False)
    address1 = models.TextField(null=False)
    address2 = models.TextField(null=True)
    country = models.CharField(max_length=150, choices=COUNTRY_CHOICES , null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    zip_code = models.CharField(max_length=10, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default="PENDING")
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f"Id: {self.id} Tracking no:  {self.tracking_no}"
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
class CheckoutItem(AbstractBaseModel):
    checkout = models.ForeignKey(
        "order.Checkout",
        on_delete=models.CASCADE,
        related_name="checkout"
    )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="product"

    )

    size = models.CharField(
        _('Size'),
        choices=SIZE_CHOICE,
        max_length=10,
        null=True, )

    color = models.CharField(
        _('Color'),
        max_length=20,
        choices=COLOR_CHOICES,
        null=True)

    price = models.FloatField(null=False)
    quantity = models.PositiveIntegerField(null=False)
    status = models.CharField(
        _("Status"),
        choices=STATUS_CHOICES,
        max_length=10,
        null=True,
    )

    def __str__(self):
        return f"ID: {self.checkout.id} Tracking no:  {self.checkout.tracking_no}"