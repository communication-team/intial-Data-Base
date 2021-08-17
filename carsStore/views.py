from django.db import reset_queries
from django.db.models.fields import NOT_PROVIDED
from django.http import request
from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permission import PermissionsClass,PermissionsClassCarInfo,PermissionsClassImages
from .models import *
from .serializer import *
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.backends import TokenBackend
from django.contrib.auth.hashers import make_password
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
            
             # {         
        return user
    # queryset=CarInfo.objects.all().filter(carModel='KIA',approved=False)
    
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "auth_user" ON "id_user_id" = "id" INNER JOIN "carsStore_cars" ON "id_cars_id" = "id_cars" ')
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "carsStore_cars" ON "id_cars_id" = "id_cars"')
    # queryset=CarInfo.objects.raw('SELECT * FROM "carsStore_carinfo" INNER JOIN "auth_user" ON "id_user_id" = "id"')
        


class CarInfoDetials(RetrieveAPIView):
    queryset=CarInfo.objects.all()
    serializer_class=CarInfoSerializer
    permission_classes = (PermissionsClass,)  


@api_view(['GET'])
def getUserIngo(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    data = {'token': token}
    
    valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
    print(valid_data)
    user = valid_data['user_id']
    request.user = user

    queryset = User.objects.get(id=int(user))
    serilizer = UserInfoSerializer(queryset)
    return Response(serilizer.data)


 
   



@api_view(['POST'])


def CarInfoCreate(request):
    print(request.data)
    serilizer = CarInfoSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response("serilizer.data")
    else:
        print('ffffffffffffffffffffffffff')
        return Response("dddd.data")



@api_view(['POST'])
def AddUser(request):
    print(make_password(request.data['password']))
    data=request.data
    data._mutable = True
    data['password']=make_password(request.data['password'])
    serilizer = UserInfoSerializer(data=data)
    if serilizer.is_valid():
        serilizer.save()
        return Response("serilizer.data")
    # else:
    #     return Response("no")

    

# class CarInfoCreate(CreateAPIView,PermissionsClassCarInfo):# here 
#     permission_classes = (PermissionsClassCarInfo,)
#     queryset=CarInfo.objects.all()
#     serializer_class=CarInfoSerializer
#     # permission_classes = (PermissionsClass,)


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
    # parser_classes = [MultiPartParser,FormParser]
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
