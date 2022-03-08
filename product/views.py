from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics
from rest_framework.viewsets import ModelViewSet

from product.models import Category, Product
from product.serializer import CategorySerializer, ProductSerializer

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ["name","category__name","category__category__name"]
    filterset_fields = ["category","category__category"]

    def update(self, request, *agrs, **kwargs):
        kwargs['partial'] = True
        return super().update(request,*agrs,**kwargs)