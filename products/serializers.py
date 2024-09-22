from .models import Product, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = serializers
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = serializers
        fields = "__all__"
