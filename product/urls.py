from django.urls import path
from .views import ProductListView, product_list, product_search, category_list, sub_category_list, add_review, product_review


urlpatterns = [
    path("products", ProductListView.as_view(), name="products"),
    path("product-detail/<slug:slug>", product_list, name="product-detail"),
    path('search-product', product_search, name='product-search'),
    #category
    path("category/<slug:cat_slug>", category_list, name="categories"),
    path("category/<slug:cat_slug>/<slug:sub_slug>", sub_category_list, name="subcategories"),
    # Reviews
    path("add-reviews/<int:pid>", add_review , name='add-reviews'),
    path("product-detail/<slug:slug>/reviews/", product_review, name='product_review'),



]