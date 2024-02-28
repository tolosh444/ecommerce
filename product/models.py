from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from account.views import User
from core.abstact_models import AbstractBaseModel
from core.choices import (COLOR_CHOICES, PRICE_CURRENCY, RATING_CHOICES,
                          SIZE_CHOICE)

# Create your models here.



class Product(AbstractBaseModel):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    original_price = models.DecimalField(_('org Price'), null=True, blank=True, max_digits=19, decimal_places=2)
    selling_price = models.DecimalField(_('sell Price'), null=True, blank=True, max_digits=19, decimal_places=2)
    price_currency = models.CharField(_('Price_currency'), choices=PRICE_CURRENCY, max_length=10)
    quantity = models.IntegerField(null=False, blank=False)
    size = models.CharField(_('Size'), choices=SIZE_CHOICE, max_length=10)
    color = models.CharField(_('Color'), choices=COLOR_CHOICES, null=True)
    slug = models.SlugField(_('Slug'), unique=True)
    prod_author = models.ForeignKey(
        "account.Account",
        on_delete = models.CASCADE,
        null = True,
        related_name = "auth_posts"
    )
    category = models.ManyToManyField(
        'product.Category',
        related_name='category_post'
    )
    sub_category = models.ManyToManyField(
        'product.SubCategory',
        related_name='sub_category_post'

    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ["-created_at"]



    def __str__(self):
        return self.name


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cache_name = self.name

    def save(self, *args, **kwargs):
        if self.cache_name != self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

class ProductImage(AbstractBaseModel):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name="product_img"
    )
    image = models.ImageField(
        _('Image'),
        upload_to='Product_Image'
    )

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.product.name


class Category(AbstractBaseModel):
    title = models.CharField(_('Title'), max_length=50, default='Categoties', blank=True)
    name = models.CharField(
        _('Name'), max_length=100, null=True, blank=True
    )
    # name_ru = models.CharField(_('Name English'), max_length=50, null=True, blank=True)
    image = models.ImageField(
        _('Image'),
        upload_to='Category_Image',
        null=True
    )

    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cache_name = self.name

    def save(self, *args, **kwargs):
        if self.cache_name != self.name:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class SubCategory(AbstractBaseModel):
    name = models.CharField(
        _('Name'), max_length=100
    )
    slug = models.SlugField(_('Slug'), unique=True)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cache_name = self.name

    def save(self, *args, **kwargs):
        if self.cache_name != self.name:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)



class ProductReviews(AbstractBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name="review_product"
    )
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)


    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return f"{self.user}, product: {self.product},"

    def get_rating(self):
        return self.rating
class Subscrabed(AbstractBaseModel):
    name = models.CharField(_('Name'), max_length=15, null=True)
    email = models.EmailField(_('Email'), null=True)

    class Meta:
        verbose_name = 'Subscraber'
        verbose_name_plural = 'Subscrabers'
    def __str__(self):
        return f"Name - {self.name},  Email - {self.email}"
