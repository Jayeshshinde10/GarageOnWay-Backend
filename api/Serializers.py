from .models  import *
from rest_framework.serializers import ModelSerializer
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ServiceProviderSerializer(ModelSerializer):
    class Meta:
        model = ServiceProvider  # Use '=' instead of ':'
        fields = '__all__'  # Use '=' instead of ':'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model= Customer
        fields='__all__'

class VehicleSerializer(ModelSerializer):
    class Meta:
        model= Vehicles
        fields='__all__'