from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
     
     ROLES=[("TENANT","Tenant"),("LANDLORD","Landlord")]
     role=models.CharField(choices=ROLES ,blank=False ,max_length=50)

