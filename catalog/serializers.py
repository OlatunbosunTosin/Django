from rest_framework import serializers

from .models import Product, Category, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'sku']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id','name', 'products']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_id']
