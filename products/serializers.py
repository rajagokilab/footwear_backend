from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # this ensures full URL

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'rating', 'msrp', 'price', 'colors', 'category', 'image','style', 'size',]
