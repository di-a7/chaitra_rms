from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoryApiView)
router.register(r'foods', FoodViewset)
urlpatterns = [
   path('tables/',TableViewSet.as_view({'get':'list','post':'create'})),
   path('tables/<int:number>/',TableViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
] + router.urls
