# orders/serializers.py
from rest_framework import serializers
from .models import Order
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'images']

    def get_images(self, obj):
        # If your Product model has a single ImageField called 'image'
        if hasattr(obj, 'image') and obj.image:
            return [obj.image.url]
        # If using multiple images through a related model, adjust accordingly
        return []

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Nest ProductSerializer

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'product', 'quantity', 'total_price', 'status', 'created_at']
