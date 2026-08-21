from rest_framework import serializers
from .models import Maintanance

class unit_maintanance_serializer(serializers.ModelSerializer):
      class Meta:
            model=Maintanance
            fields=["unit_id","property_units","Maintanance_issue","Maintanance_priority","created_at","assignment_status"]

      def create_maintanance(sef,validated_data):
            maintanance=Maintanance.objects.create(**validated_data)