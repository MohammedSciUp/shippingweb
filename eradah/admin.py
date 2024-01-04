from django.contrib import admin
from .models import ShippingRate, ContainerLaunch,Order
# Register your models here.



admin.site.register(ShippingRate)
admin.site.register(ContainerLaunch)
admin.site.register(Order)
