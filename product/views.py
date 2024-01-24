from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from order.models import Wishlist, Order
from .models import Product, Category, SubCategory, ProductReviews
from core.utils.helpers import get_values_from_choices
from core.choices import SIZE_CHOICE, COLOR_CHOICES, RATING_CHOICES
from django.db.models import Q, Avg
from .forms import ProductReviewForm


class ProductListView(ListView):
    #pagination
    paginate_by = 6
    model = Product
    template_name = "products/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wishlist_count"] = Wishlist.objects.filter(user=self.request.user.id).count()
        context["shopping_count"] = Order.objects.filter(user=self.request.user.id).count()

        context["categories"]  = Category.objects.all()
        context["sub_categories"] = SubCategory.objects.all()

        return context


# def products(request):
#     products = Product.objects.all().order_by("-created_at")[:9]
#
#     context = {
#         "products": products,
#     }
#     return render(request, "products/products.html", context)

def product_list(request, slug):

    # Cat and SubCat for navbar dropdown
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    # Products details
    product_det = Product.objects.get(slug=slug)
    product_quantity = product_det.quantity

    # You may like in details page
    category_ids = [obj.id for obj in product_det.category.all()]
    subcategory_ids = [obj.id for obj in product_det.sub_category.all()]
    you_like = Product.objects.filter(category__in=category_ids, sub_category__in=subcategory_ids).distinct()[:8]



    # Counting wishlist and basket
    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    # Size and Color choices
    sizes = get_values_from_choices(SIZE_CHOICE)
    colors = get_values_from_choices(COLOR_CHOICES)
    rating = get_values_from_choices(RATING_CHOICES)

    # Review form for Product
    review_form = ProductReviewForm()

    pro_reviews = ProductReviews.objects.filter(product=product_det).order_by("-created_at")[:3]
    review_count = pro_reviews.count()

    if request.method == "GET":
        review_form = ProductReviewForm(initial={'product': product_det})

    else:
        review_form = ProductReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product_det
            review.save()
            messages.success(request, "Thank you for your review!")
        else:
            messages.error(request, "Something went wrong with your review!")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





    context = {
        "pro_reviews": pro_reviews,
        "review_count": review_count,
        "review_form": review_form,
        "ratings": rating,
        "product_det": product_det,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "categories": categories,
        "sub_categories": sub_categories,
        "you_like": you_like,
        "sizes": sizes,
        "colors": colors,
        "product_quantity": product_quantity

    }

    return render(request, "products/details.html", context)



def product_review(request, slug):
    # Review form for Product
    review_form = ProductReviewForm()
    product_detail = get_object_or_404(Product, slug=slug)
    pro_reviews = ProductReviews.objects.filter(product=product_detail).order_by("-created_at")
    review_count = pro_reviews.count()

    # Counting wishlist and basket
    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    # Cat and SubCat for navbar dropdown
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()


    # Pagination
    paginator = Paginator(pro_reviews, 3)  # Show 3 reviews per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        pro_reviews = paginator.page(page_number)
    except PageNotAnInteger:
        pro_reviews = paginator.page(1)
    except EmptyPage:
        pro_reviews = paginator.page(paginator.num_pages)

    if request.method == "GET":
        review_form = ProductReviewForm(initial={'product': product_detail})

    else:
        review_form = ProductReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product_detail
            review.save()
            messages.success(request, "Thank you for your review!")
        else:
            messages.error(request, "Something went wrong with your review!")

        return HttpResponseRedirect("/")

    context = {
        "pro_reviews": pro_reviews,
        "product_detail": product_detail,
        "review_form": review_form,
        "review_count": review_count,
        "page_obj": page_obj,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "categories": categories,
        "sub_categories": sub_categories,


    }
    return render(request, "products/reviews.html", context)


def product_search(request):

    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    searched = request.GET['searched']

    if not searched:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    searched_products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(category__name__icontains=searched) | Q(sub_category__name__icontains=searched)).distinct()



    page = request.GET.get('page', 1)
    paginator = Paginator(searched_products, 6)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        # main
        "searched_products_count": len(searched_products),
        'searched': searched,
        'page_obj': products,
        # other
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "categories": categories,
        "sub_categories": sub_categories,
    }
    return render(request, "products/search.html", context)




def category_list(request, cat_slug):
    cat_det = get_object_or_404(Category, slug=cat_slug)
    products = Product.objects.filter(category=cat_det)


    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()

    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    # Pgination
    paginator = Paginator(products, 6)  # Show 6 reviews per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "cat_det": cat_det,
        "products": products,
        "categories": categories,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "sub_categories": sub_categories,
        "page_obj": page_obj

                }
    return render(request, 'products/category_detail.html', context)



def sub_category_list(request, cat_slug, sub_slug):

    categories = Category.objects.all()

    sub_categories = SubCategory.objects.all()
    category = get_object_or_404(Category, slug=cat_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_slug)
    sub_products = Product.objects.filter(sub_category=subcategory)


    wishlist_count = Wishlist.objects.filter(user=request.user.id).count()
    shopping_count = Order.objects.filter(user=request.user.id).count()

    # Pgination
    paginator = Paginator(sub_products, 6)  # Show 6 reviews per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        sub_products = paginator.page(page_number)
    except PageNotAnInteger:
        sub_products = paginator.page(1)
    except EmptyPage:
        sub_products = paginator.page(paginator.num_pages)




    context = {

        'category': category,
        "sub_categories": sub_categories,
        'subcategory': subcategory,
        "wishlist_count": wishlist_count,
        "shopping_count": shopping_count,
        "sub_products": sub_products,
        "categories": categories,
        "page_obj": page_obj
                }
    return render(request, "products/subcategory_detail.html", context)

def add_review(request, pid):
    product = get_object_or_404(Product, id=pid)
    user = request.user
