from rest_framework.routers import SimpleRouter

from .views import (ProfileViewSet, OrderViewSet, OrderItemsViewSet,
                    CategoryViewSet, ProductViewSet, ReviewViewSet)

router = SimpleRouter()

router.register('profiles', ProfileViewSet, basename='profiles')
router.register('orders', OrderViewSet, basename='orders')
router.register('orderitems', OrderItemsViewSet, basename='orderitems')
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductViewSet, basename='products')
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls
