from django.db import models

# Create your models here.
class Unit_property(models.Model):
     UNIT_STATUSES={("Occupied","Occupied"),("Maintanance","Maintanance"),("Vacant","Vacant")}

     unit_id=models.CharField(primary_key=True,default="U-0000")
     property_name=models.CharField(blank=False,max_length=100)
     property_units=models.CharField(max_length=50,unique=False,blank=False)
     tenant=models.CharField(max_length=50,blank=False)
     status=models.CharField(choices=UNIT_STATUSES,blank=False ,default="Vacant")
     rent_amount=models.PositiveIntegerField()
     lease_start=models.DateField()
     lease_end=models.DateField()


     def __str__(self):
         return f"{self.unit_id}{self.property_name}"
     

