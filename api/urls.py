from django.urls import path

from .views import (ProfileList, ProfileDetail, OrderList, OrderDetail, OrderItemsList, OrderItemsDetail,
                    CategoryList, CategoryDetail, ProductList, ProductDetail, ReviewList, ReviewDetail)

app_name = 'api'


urlpatterns = [
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('order/', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('orderitems/', OrderItemsList.as_view(), name='orderitems_list'),
    path('orderitems/<int:pk>/', OrderItemsDetail.as_view(), name='orderitems_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('product/', ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
]
