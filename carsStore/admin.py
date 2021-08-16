from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.




admin.site.register(MyAppUser)
# admin.site.register(Cars)
admin.site.register(CarInfo)
admin.site.register(Images)
admin.site.register(Post)
admin.site.register(FeedBack)