from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rms.models import Category
from .serializers import CategorySerializer

# Create your views here.
@api_view()
def category(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response({serializer.data})

@api_view()
def table(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response({serializer.data})