from .models import Maintanance
from .serializers import unit_maintanance_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(["POST"])
def create_maintanance_view(request):
    serializer=unit_maintanance_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def list_maintanance_view(request):
    maintanance_data=Maintanance.objects.all()
    serializer=unit_maintanance_serializer(maintanance_data,many=True)
    
    return Response(serializer.data,status=status.HTTP_200_OK)


