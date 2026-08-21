from django.db import models
from landlords.models import Unit_property


class Maintanance(models.Model):
     PRIORITIES=[("Medium","Medium"),("Low","Low"),("Urgent","Urgent")]

     unit_id=models.ForeignKey(Unit_property,on_delete=models.CASCADE)
     property_units=models.CharField(max_length=50,unique=False,blank=False)
     Maintanance_issue=models.CharField(max_length=500)
     Maintanance_priority=models.CharField(choices=PRIORITIES)
     created_at=models.DurationField()
     assignment_status=models.CharField(max_length=100,default="Unassigned")

     def __str__(self):
         return f"{self.unit_id}{self.assignment_status}"
     