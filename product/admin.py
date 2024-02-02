from django.contrib import admin
from .models import Product, ProductImage, Category, SubCategory, ProductReviews, Subscrabed
# Register your models here.

admin.site.register(ProductReviews)
admin.site.register(Subscrabed)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
class PointInlineAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1
@admin.register(Product)
class ProductImgAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [PointInlineAdmin]
    prepopulated_fields = {'slug': ('name',)}
