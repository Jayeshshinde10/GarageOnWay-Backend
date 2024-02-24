from django.contrib import admin
from .models import *
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["latitude", "longitude","Customer_id"]
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display =[]
# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Order)

