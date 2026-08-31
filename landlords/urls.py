from .views import create_unit_property_view,unit_property_list,get_unit_property,update_unit_property,create_property_view
from django.urls import path

urlpatterns = [
    path('create/unit',create_unit_property_view, name="create_unit" ),
    path('list/units',unit_property_list, name="unit_list" ),
    path('list/units/<str:unit_id>',get_unit_property, name="get_unit" ),
    path('list/units/update/<str:unit_id>',update_unit_property, name="update_unit" ),
    path('list/units/delete/<str:unit_id>',update_unit_property, name="delete_unit" ),
    path('create/property',create_property_view, name="create_property" ),

]