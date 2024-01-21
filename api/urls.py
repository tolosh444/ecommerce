from django.urls import path, include
from .views import ProductCreateAPIView, ProductDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('api/product/create', ProductCreateAPIView.as_view(), name="create-product"),
    path("api/product/detail/<int:id>",
         ProductDetailAPIView.as_view(),
         name="product-detail",
         ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
