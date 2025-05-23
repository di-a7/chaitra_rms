from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.serializers import ValidationError
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView,ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from .filters import FoodFilter
from .permission import IsAuthenticatedOrReadonly
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

# class CategoryList(ListCreateAPIView):
#    queryset = Category.objects
#    serializer_class = CategorySerializers

# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializers
#    lookup_field = 'id'
   
#    def destroy(self,request,id):
#       category = get_object_or_404(Category,id=id)
#       count = OrderItem.objects.filter(food__category = category).count()
#       if count > 0:
#          return Response({
#             "detail":"OrderItem with this category exist. This category cannot be deleted."
#          })
#       category.delete()
#       return Response({
#          "detail":"Category has been deleted."
#       }, status=status.HTTP_204_NO_CONTENT)

class CategoryApiView(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializers
   permission_classes = [IsAuthenticatedOrReadonly]
   
   def list(self, request):
      queryset = Category.objects.all()
      serializer = CategorySerializers(queryset, many=True)
      return Response({'data':serializer.data})
   
   def destroy(self,request,pk):
      category = get_object_or_404(Category,id=pk)
      count = OrderItem.objects.filter(food__category = category).count()
      if count > 0:
         return Response({
            "detail":"OrderItem with this category exist. This category cannot be deleted."
         })
      category.delete()
      return Response({
         "detail":"Category has been deleted."
      }, status=status.HTTP_204_NO_CONTENT)
      

class FoodViewset(ModelViewSet):
   queryset = Food.objects.select_related().all()
   serializer_class = FoodSerialaizers
   pagination_class = PageNumberPagination
   filter_backends = (filters.SearchFilter,filter.DjangoFilterBackend)
   filterset_class  = FoodFilter
   search_fields = ('name',)
   permission_classes = [IsAuthenticatedOrReadonly]


class TableViewSet(ModelViewSet):
   queryset = Table.objects.all()
   serializer_class = TableSerialzier
   lookup_field = 'number'