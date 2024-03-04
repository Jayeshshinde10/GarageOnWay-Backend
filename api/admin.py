from django.contrib import admin
from django.utils.html import format_html
from .models import *
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["latitude", "longitude","Customer_id"]
class ServiceProviderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display =['image1','image2','orginazation_name','near_by_landmark']


class VehiclesAdmin(admin.ModelAdmin):
    list_display =["vehicle_name"]

# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(ServiceProvider,ServiceProviderAdmin)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Vehicles,VehiclesAdmin)

