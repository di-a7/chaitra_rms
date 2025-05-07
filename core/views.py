from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.
class LoginAPIView(APIView):
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      if username == None and password == None:
         raise ValidationError({
            "details":"Both Username and Password are required."
         })
      user = authenticate(username = username,password=  password)
      if user:
         token,_=Token.objects.get_or_create(user=user)
         return Response({
            "token":token.key,
            "username":user.username
         },status=status.HTTP_202_ACCEPTED)
      return Response({
         "details":"User is not registerd."
      }, status=status.HTTP_401_UNAUTHORIZED)