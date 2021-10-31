from django.urls import path

from .views import product_list, product_detail, product_search

app_name = 'shops'


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>', product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', product_detail, name='product_detail'),
    path('search/', product_search, name='product_search'),
]
