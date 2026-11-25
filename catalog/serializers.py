from rest_framework import serializers

from .models import Product, Category, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'sku']

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id','name', 'products']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [ 'product', 'quantity','total_price']

    def get_total_price(self, item: CartItem):
        return item.quantity * item.product.price


class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['cart_id', 'items', 'total']

    def get_total(self, cart: Cart):
       return sum(cart_item.quantity * cart_item.product.price for cart_item in cart.items.all())



