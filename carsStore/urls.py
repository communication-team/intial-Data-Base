

from django.urls import path
from .views import *
urlpatterns = [

    path('feedback', FeedBackList.as_view(),name='FeedBack'),
    path('feedback/create/',FeedBackCreate.as_view(),name='FeedBack_create'),
    path('feedback/<int:pk>/',FeedBackDetials.as_view(),name='FeedBack_detials'),  


    # path('cars', CarsList.as_view(),name='Cars'),
    # path('cars/create/',CarsCreate.as_view(),name='Cars_create'),
    # path('cars/<int:pk>/',CarsDetials.as_view(),name='Cars_detials'), 


    path('carinfo', CarInfoList.as_view(),name='CarInfo'),
    path('carinfo/create/',CarInfoCreate.as_view(),name='CarInfo_create'),
    path('carinfo/<int:pk>/',CarInfoDetials.as_view(),name='CarInfo_detials'),  
    path('carinfo/all_access/<int:pk>/',CarInfoAllOpreations.as_view(),name='CarInfo_detials_all_access'),

    # images part 
    path('images', ImagesList.as_view(),name='Images'),
    path('images/create/',ImagesCreate.as_view(),name='Images_create'),
    path('images/<int:pk>/',ImagesDetials.as_view(),name='Images_detials'), 
    # path(we need to add new path for delete or updata), 

    # post part 

    path('post',PostList.as_view(),name='Post'),
    path('post/create/',PostCreate.as_view(),name='Post_create'),
    path('post/<int:pk>/',PostDetials.as_view(),name='Post_detials'),  
]
