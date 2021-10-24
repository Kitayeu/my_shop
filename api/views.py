from rest_framework import generics

from accounts.models import Profile
from orders.models import Order, OrderItems
from shops.models import Category, Product, Review

from .serializers import (ProfileSerializer, OrderSerializer, OrderItemsSerializer,
                          CategorySerializer, ProductSerializer, ReviewSerializer)


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemsList(generics.ListAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class OrderItemsDetail(generics.RetrieveAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
