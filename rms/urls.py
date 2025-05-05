from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryApiView)
router.register(r'foods', FoodViewset)
urlpatterns = [
   # path('category',CategoryApiView.as_view({'get':'list','post':'create'})),
   # path('category/<int:pk>/',CategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
] + router.urls
