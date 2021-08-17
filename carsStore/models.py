from django.db import models



from django.contrib.auth.models import User

class MyAppUser( models.Model ) :
    # def __unicode__( self ) :
    #    return self.user.username

    user = models.ForeignKey( 'auth.User',
    on_delete=models.CASCADE, )
        

    gender = models.BooleanField(default=True)
    role = models.TextField(max_length=10, blank = True )
    phone   = models.CharField( max_length = 135, blank = True )

# class Cars(models.Model):
#     id_cars=models.AutoField(primary_key=True)
#     carModel=models.CharField(max_length=200)
#     def __str__(self):
#         return self.carModel

class CarInfo(models.Model):
    id_info=models.AutoField(primary_key=True)
    carModel=models.CharField(max_length=200,null=True) 
    # id_user=models.ForeignKey('auth.User',related_name='user', blank=True,on_delete=models.CASCADE)
    id_user=models.ForeignKey('auth.User',related_name='user',null=True, blank=True,on_delete=models.CASCADE)
    phone   = models.CharField( max_length = 135,null=True)
    user_name   = models.CharField( max_length = 135,null=True )
    title=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    transmission=models.CharField(max_length=20) 
    cylinder=models.CharField(max_length=200)
    fuel=models.CharField(max_length=20)
    engine_size=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    documents=models.CharField(max_length=200)
    insurance=models.CharField(max_length=200)
    km=models.CharField(max_length=200)
    approved=models.CharField(max_length=200)
    price=models.CharField( max_length=200)
    payment_type=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    image1=models.TextField()
    image2=models.TextField()
    image3=models.TextField()
    image4=models.TextField()
    primary_image=models.TextField()

   
    def __str__(self):
        return self.title
   
def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)
class Images(models.Model):
    id_images=models.AutoField(primary_key=True)
    # image=models.TextField()
    image=models.ImageField('Image',upload_to=upload_to,null=False)
    id_info=models.ForeignKey(CarInfo,blank=True,null=True,on_delete=models.CASCADE)
    # id_info=models.ForeignKey(CarInfo,blank=True,on_delete=models.CASCADE)

class Post(models.Model):
    id_post=models.AutoField(primary_key=True)
    id_info=models.ForeignKey(CarInfo , blank=True,null=True , on_delete=models.CASCADE)
    # id_info=models.ForeignKey(CarInfo , blank=True , on_delete=models.CASCADE)
    text = models.TextField()

class FeedBack(models.Model):
    id_feedback=models.AutoField(primary_key=True)
    text = models.TextField(max_length=500)
    sender_name=models.CharField(max_length=200)
    id_user=models.ForeignKey('auth.User', blank=True,null=True, on_delete=models.CASCADE)
    # id_user=models.ForeignKey('auth.User', blank=True, on_delete=models.CASCADE)
    email=models.CharField(max_length=200)
