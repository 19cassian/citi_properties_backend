from django.urls import path
from .views import create_maintanance_view,list_maintanance_view

urlpatterns = [
    path('create',create_maintanance_view, name="create_maintanance" ),
    path('list',list_maintanance_view, name="list_maintanance" ),

    

]