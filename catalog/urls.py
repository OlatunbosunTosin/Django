from django.urls import path, include
from .views import ProductViewSet, get_product_by_category, CartViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('carts', CartViewSet, basename='cart')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/<slug:slug>/', get_product_by_category, name='category_products_list'), #pathvariable
]
urlpatterns += router.urls