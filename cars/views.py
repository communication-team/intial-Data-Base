from django.shortcuts import render
from django.db import models
from rest_framework import generics, serializers
from .models import CarInfo
from .serializers  import CarInfoSerializer 
# from .permissions import IsAuthorOrReadOnly

# Create your views here.
class homePage(generics.ListAPIView):#serializers=>  foramt the data to send it in right way to next.js
    queryset = CarInfo.objects.all()
    serializer_class= CarInfoSerializer
    pass # continue from here 