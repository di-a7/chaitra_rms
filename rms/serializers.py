from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      # category = Category.objects.all()
      category_count = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if category_count > 0 :
         raise serializers.ValidationError({
            "detail":"Category already exist."
         })
      category = Category(**validated_data)
      category.save()
      return category


class FoodSerialaizers(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = Category.objects.all(),
      source = 'category'
   )
   class Meta:
      model = Food
      fields = [
         'id',
         "name",
         "price",
         "price_with_tax",
         "category_id",
         "category"]
   
   def get_price_with_tax(self,food:Food):
      return food.price*0.13 + food.price

class TableSerialzier(serializers.ModelSerializer):
   class Meta:
      model = Table
      fields = '__all__'