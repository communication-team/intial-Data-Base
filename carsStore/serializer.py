from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import *

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id_user','text','sender_name','email')
        model=FeedBack


      
  
# class CarsSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields=('carModel',)
#         model=Cars


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('image','id_info')
        model=Images


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('text','id_info')
        model=Post




class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CarInfo
        fields="__all__"


class CarInfoSerializer(serializers.ModelSerializer):
   

    class Meta:
        model=CarInfo
        fields="__all__"
        
class UserInfoSerializer(serializers.ModelSerializer):
   

    class Meta:
        model=User
        fields="__all__"
     
        # fields=('user','id_info','id_cars_id','id_user_id','brand','year','color','transmission','cylinder','fuel','engine_size','status','documents','insurance','km','approved','price','payment_type','location')
 



