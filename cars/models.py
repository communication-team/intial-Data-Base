from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

choices=['personal','Business']
trans=['Manual','Automatic']
fuel=['Diesel Fuel','benzine','hybrid','electric']
paymentMethod=['Cash','installments']
class UserAccount(models.Model):# change it to account
    id_user=models.IntegerField()
    name = models.CharField(max_length=200)
    email= models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)# maybe on_delete=models.RESTRICT
    email= models.EmailField(max_length=200 , unique=True)
    password=models.CharField(max_length=200)
    role = models.CharField( max_length=10)
    phone = models.CharField(max_length=20)

class Cars(models.Model):
    id_cars=models.IntegerField()
    carModel=models.CharField(max_length=200)

class CarInfo(models.Model):
    id_info=models.IntegerField()
    id_cars=models.ForeignKey(Cars , blank=True,null=True,on_delete=models.CASCADE)   
    brand=models.CharField(max_length=200)
    year=models.IntegerField(default=2021)
    color=models.CharField(max_length=200)
    transmission=models.CharField(max_length=20) 
    cylinder=models.IntegerField(default=4)
    fuel=models.CharField(max_length=20)
    engine_size=models.IntegerField(default=1600)
    status=models.BooleanField(default=False)
    documents=models.CharField(max_length=200)
    insurance=models.CharField(max_length=200)
    km=models.IntegerField()
    id_user=models.ForeignKey(UserAccount, blank=True,null=True,on_delete=models.CASCADE)
    approved=models.BooleanField()
    price=models.PositiveIntegerField(
        verbose_name=("price"),
        help_text=("min price is 1000 JD"),
        validators=[MinValueValidator(1000)],
        error_messages={
            "name":{
                "min_price":("the price must be more than 1000 JD"),
            },
        },
    )
    payment_type=models.IntegerField()
    location=models.CharField(max_length=200)
    show=models.BooleanField(default=False)# if the product is new and we are in new page show , otherwise hide

class Images(models.Model):
    images_id=models.IntegerField()
    image=models.CharField(max_length=300)
    # image =models.ImageField(
    #     verbose_name=("image"),
    #     height_field=("upload a car image"),
    #     upload_to="images/",
    #     default="images/defualt.png"
    # )
    id_info=models.ForeignKey(CarInfo,blank=True,null=True,on_delete=models.CASCADE)



class Post(models.Model):
    post_id=models.IntegerField()
    id_info=models.ForeignKey(CarInfo , blank=True,null=True , on_delete=models.CASCADE)
    text = models.TextField(max_length=500)


class FeedBack(models.Model):
    feedback_id=models.IntegerField()
    text = models.TextField(max_length=500)
    sender_name=CharField(max_length=200)
    id_user=models.ForeignKey(UserAccount, blank=True,null=True, on_delete=models.CASCADE)
    email=models.EmailField(max_length=200)





    



    def get_absolute_url(self):
        return reverse('car_list')

    def __str__(self):
        return self.name