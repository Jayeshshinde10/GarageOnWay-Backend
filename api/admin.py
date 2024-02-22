from django.contrib import admin
from .models import *
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "view_birth_date"]

# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Order)

