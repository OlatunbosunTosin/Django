from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import ProductSerializer, CategorySerializer, CartSerializer
from .models import Product, Category, Cart
from rest_framework.generics import ListAPIView, RetrieveAPIView


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAdminUser()]

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_product_by_category(request,slug):
    category = get_object_or_404(Category, slug=slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all().filter(is_active=True)
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data, status=HTTP_200_OK)

class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


