from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rms.models import Category, Inventory, Table
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