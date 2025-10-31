from rest_framework import serializers
from .models import Category, Tag, Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'alt', 'order')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ('id','title','slug','description','price','category','tags','is_published','owner','created_at','updated_at','images')
