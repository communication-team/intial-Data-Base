from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import CarInfo

class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:# we need to show info from user as will in the same page
        model = CarInfo
        fields = ['brand','year','color','transmission','cylinder','fuel','engine_size','status','documents','insurance','km','price','payment_type','location']