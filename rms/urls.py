from django.urls import path, include
from .views import *
urlpatterns = [
   path('category',CategoryApiView.as_view({'get':'list','post':'create'})),
   path('category/<int:pk>/',CategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
]
