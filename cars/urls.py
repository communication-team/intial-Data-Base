from django.conf.urls import url
from django.urls import path,include
from .views import homePage 
urlpatterns = [# api/v1/cars/
    path('',homePage.as_view(),name="homeStore")
    # path('new/',carsNewListView.as_view(),name='newList'),
    # path('used/',carsUesdListView.as_view(),name='usedList'),
]