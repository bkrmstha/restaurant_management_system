from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        # Category.objects.create(name=validated_data.get('name'))
        return category
    

class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    is_available = serializers.BooleanField()
    reservation = serializers.DateTimeField()

class InventorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    stock = serializers.IntegerField()
    minimum_stock = serializers.IntegerField()
