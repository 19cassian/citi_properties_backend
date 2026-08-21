from django.urls import path
from .views import create_maintanace_view

urlpatterns = [
    path('create',create_maintanace_view, name="create_maintanance" ),
    

]