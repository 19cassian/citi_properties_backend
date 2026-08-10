from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.serializer):
      class Meta:
            fields=['username','email','passowrd','first_name','last_name','role']

#Overiding the save method for the User instance
      def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')
        role = validated_data.get('role')
        user =CustomUser.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,role=role)
        user.save()
        return user