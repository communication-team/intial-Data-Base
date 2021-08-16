from django.db import reset_queries
from django.db.models.fields import NOT_PROVIDED
from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .permission import PermissionsClass,PermissionsClassCarInfo,PermissionsClassImages
from .models import *
from .serializer import *
from django.db.models import Q

class FeedBackList(ListAPIView):
    # queryset=FeedBack.objects.all()
    queryset=FeedBack.objects.raw('SELECT * FROM "carsStore_feedback"')
    permission_classes = (PermissionsClass,)
    serializer_class=FeedBackSerializer

class FeedBackDetials(RetrieveAPIView):
    queryset=FeedBack.objects.all()
    serializer_class=FeedBackSerializer
    permission_classes = (PermissionsClass,)


class FeedBackCreate(CreateAPIView):
    queryset=FeedBack.objects.all()
    serializer_class=FeedBackSerializer
    permission_classes = (PermissionsClass,)

class FeedBackAllOpreations(RetrieveUpdateDestroyAPIView):
    queryset=FeedBack.objects.all()
    serializer_class=FeedBackSerializer
    permission_classes = (PermissionsClass,)

# class CarsList(ListAPIView):
#     queryset=Cars.objects.all()
#     serializer_class=CarsSerializer

# class CarsDetials(RetrieveAPIView):
#     queryset=Cars.objects.all()
#     serializer_class=CarsSerializer


# class CarsCreate(CreateAPIView):
#     queryset=Cars.objects.all()
#     serializer_class=CarsSerializer
#     # permission_classes = (PermissionsClass,)



class CarInfoList(ListAPIView):
    serializer_class=CarInfoSerializer  
    permission_classes = (PermissionsClass,)  
    def get_queryset(self,*args,**kwargs):
        user = CarInfo.objects.all()
        queryset2 = self.request.GET
        temp={}
        for x in queryset2:
            temp[x]=queryset2[x]
            print(f'{x} {queryset2[x]} ')
        print(queryset2)
        print(temp)
        if queryset2:          
            user=user.filter(**temp)           
        return user
    # queryset=CarInfo.objects.all().filter(carModel='KIA',approved=False)
    
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "auth_user" ON "id_user_id" = "id" INNER JOIN "carsStore_cars" ON "id_cars_id" = "id_cars" ')
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "carsStore_cars" ON "id_cars_id" = "id_cars"')
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "auth_user" ON "id_user_id" = "id"')
        


class CarInfoDetials(RetrieveAPIView):
    queryset=CarInfo.objects.all()
    serializer_class=CarInfoSerializer
    permission_classes = (PermissionsClass,)  


class CarInfoCreate(CreateAPIView,PermissionsClassCarInfo):# here 
    permission_classes = (PermissionsClassCarInfo,)
    queryset=CarInfo.objects.all()
    serializer_class=CarInfoSerializer
    # permission_classes = (PermissionsClass,)


class CarInfoAllOpreations(RetrieveUpdateDestroyAPIView):
    queryset=CarInfo.objects.all()
    serializer_class=CarInfoSerializer
    permission_classes = (PermissionsClass,)


class ImagesList(ListAPIView):
    queryset=Images.objects.all()
    serializer_class=ImagesSerializer

class ImagesDetials(RetrieveAPIView):
    queryset=Images.objects.all()
    serializer_class=ImagesSerializer


class ImagesCreate(CreateAPIView,PermissionsClassImages):
    permission_classes = (PermissionsClassImages,)
    queryset=Images.objects.all()
    serializer_class=ImagesSerializer


class ImagesAllOpreations(RetrieveUpdateDestroyAPIView):
    queryset=Images.objects.all()
    serializer_class=ImagesSerializer
    permission_classes = (PermissionsClass,)


    
class PostList(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostDetials(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer


class PostCreate(CreateAPIView,PermissionsClassImages):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = (PermissionsClassImages,)


class PostAllOpreations(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = (PermissionsClassImages,)
