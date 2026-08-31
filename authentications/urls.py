from django.urls import path
from .views import create_user_view,tenant_list

urlpatterns = [
    path('signup/', create_user_view, name='createuser'),
    path('tenants/', tenant_list, name='tenants'),

]