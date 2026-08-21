from rest_framework import serializers
from .models import Unit_property

class property_unit_serilizer(serializers.ModelSerializer):
      class Meta:
            model=Unit_property
            fields=['unit_id','property_name','rent_amount','tenant','status','lease_start','lease_end','property_units']

      def creat_unit(self, validated_data):
           unit=Unit_property.objects.create(**validated_data)
           unit.save()
           return unit