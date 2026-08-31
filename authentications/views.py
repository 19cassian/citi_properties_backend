from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser




from django_rest_passwordreset.signals import reset_password_token_created


@api_view(["POST"])
def create_user_view(request):  
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def tenant_list(request):
     tenant=CustomUser.objects.filter(role="tenant")
     serializer=UserSerializer(tenant,many=True)
     return Response(serializer.data,status=status.HTTP_200_OK)


