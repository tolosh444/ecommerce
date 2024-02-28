from django.urls import path

from .views import OrderCreateAPIView, OrderDetailAPIView

urlpatterns = [
    path(
        "orders/create/",
        OrderCreateAPIView.as_view(),
        name="order-create",
    ),
    path("orders/detail/<int:id>",
         OrderDetailAPIView.as_view(),
         name="orders-detail",
         ),
]