from django.contrib import admin
from .models import Unit_property,Property,LandlordProfile


# Register your models here.
admin.site.register(Unit_property)
admin.site.register(Property)
admin.site.register(LandlordProfile)