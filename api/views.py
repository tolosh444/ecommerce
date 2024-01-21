from django.shortcuts import render
from django.utils.text import slugify
from rest_framework import generics, permissions, status
from product.models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        slug = slugify(name)
        serializer.save(slug=slug)
        instance = serializer.save(prod_author=self.request.user)
        return instance

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]