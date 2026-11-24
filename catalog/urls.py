from django.urls import path
from .views import ProductViewSet, get_product_by_category
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('categories/<slug:slug>/', get_product_by_category, name='category_products_list'), #pathvariable
]
urlpatterns += router.urls