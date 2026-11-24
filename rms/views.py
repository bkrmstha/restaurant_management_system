from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rms.models import Category, Inventory, Table, Order_Item
from .serializers import CategorySerializer, TableSerializer, InventorySerializer

# Create your views here.
@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        items = Order_Item.objects.filter(menu__category = category).count()
        if items > 0:
            return Response({"message": "This category can not be deleted. Being referred to menu that exists in order items."})
        category.delete()
        return Response({"message": "Data has been deleted successfully."})


@api_view()
def table(request):
    queryset = Table.objects.all()
    serializer = TableSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def inventory(request):
    queryset = Inventory.objects.all()
    serializer = InventorySerializer(queryset, many=True)
    return Response(serializer.data)