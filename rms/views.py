from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer
from rest_framework.serializers import ValidationError
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def category_list(request):
   if request.method == "GET":
      category = Category.objects.all()
      serializer = CategorySerializer(category, many=True)
      return Response(serializer.data)
   
   elif request.method == 'POST':
      serializer = CategorySerializer(data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({
         "detail":"New Category created."
      }, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','PUT', 'PATCH'])
def category_detail(request,id):
   if request.method == 'GET':
         category = get_object_or_404(Category,id=id)
         serializer = CategorySerializer(category)
         return Response(serializer.data)

   elif request.method == 'DELETE':
         category = get_object_or_404(Category,id=id)
         count = OrderItem.objects.filter(food__category = category).count()
         if count > 0:
            return Response({
               "detail":"OrderItem with this category exist. This category cannot be deleted."
            })
         category.delete()
         return Response({
            "detail":"Category has been deleted."
         }, status=status.HTTP_204_NO_CONTENT)
   
   elif request.method == "PUT":
      category = Category.objects.get(id = id)
      serializer = CategorySerializer(category, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
         
      else:
         return Response(serializer.errors)
   
   elif request.method == "PATCH":
      category = Category.objects.get(id = id)
      serializer = CategorySerializer(category, data=request.data, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      
