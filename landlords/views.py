from rest_framework.response import Response
from rest_framework import status
from .serializers import property_unit_serilizer,propertySerializer,LandlordProfileSerializer
from .models import Unit_property
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(["POST"])
def create_unit_property_view(request):
     serializer=property_unit_serilizer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def unit_property_list(request):
    units=Unit_property.objects.all()
    serializer=property_unit_serilizer(units, many=True)
    if request.method=='GET':
         return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_unit_property(request, unit_id):
    unit=Unit_property.objects.get(pk=unit_id)
    serializer=property_unit_serilizer(unit, many=False)
    if request.method=='GET':
         return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_unit_property(request, unit_id):
    unit=Unit_property.objects.get(pk=unit_id)
    serializer=property_unit_serilizer(unit, data=request.data,many=False)
    if serializer.is_valid():
         return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def edit_unit_property(request, unit_id):
    unit=Unit_property.objects.get(pk=unit_id)
    serializer=property_unit_serilizer(unit, data=request.data, many=False,partial=True)
    if serializer.is_valid():
         return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_unit_property(request, unit_id):
    unit=Unit_property.objects.get(pk=unit_id)
    unit.delete()
    return Response({"success":"Unit deleted successfully"},status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_property_view(request):
    serializer=propertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def landlord_profile(request):
    serializer=LandlordProfileSerializer(data=request.data)
    if serializer.is_valid(): 
       serializer.save()
       return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)