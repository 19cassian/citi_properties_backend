from rest_framework import serializers
from .models import Unit_property,Property,LandlordProfile

class property_unit_serilizer(serializers.ModelSerializer):
      class Meta:
            model=Unit_property
            fields=['unit_id','property_name','rent_amount','tenant','status','lease_start','lease_end','property_units']

      def creat_unit(self, validated_data):
           unit=Unit_property.objects.create(**validated_data)
           unit.save()
           return unit

class propertySerializer(serializers.ModelSerializer):
      class Meta:
            model=Property
            fields=['property_name','landlord_name']

      def create_property(self,validated_data):
            property=Property.objects.create(**validated_data)
            property.save()
            return property

class LandlordProfileSerializer(serializers.ModelSerializer):
       class Meta:
             model=LandlordProfile
             fields=['landlord_name','landlord_phone','property_owned']

       def create_lanlord_profile(self ,validated_data):
             landlordProfile=LandlordProfile.objects.create(**validated_data)
             landlordProfile.save()
             return landlordProfile
       