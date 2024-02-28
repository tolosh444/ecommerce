from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import ProductCreateAPIView, ProductDetailAPIView

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
