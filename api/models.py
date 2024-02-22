from django.db import models
from django.contrib.auth.models import User

class ServiceProvider(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    # image1 = models.ImageField()
    # image2 = models.ImageField()
    oraginazation_name = models.CharField(max_length=50)
    closing_time = models.TimeField()
    opening_time= models.TimeField()
    # latitude = models.DecimalField()
    # longitude = models.DecimalField()
    phone_number = models.CharField(max_length=20, blank=True, null=True, help_text="Enter your phone number")

# Create your models here.
class Customer(models.Model):
    Customer_id = models.OneToOneField(User,on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=30, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=6, null=False)
    


class Service(models.Model):
    name = models.CharField(max_length=100)
    #service provider table foreign key will come here
    serviceProvider_id = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Order(models.Model):
    Service_id = models.ForeignKey(Service,on_delete=models.CASCADE)
    ServiceProvider_id = models.ForeignKey(ServiceProvider , on_delete=models.CASCADE)
    #customer_id = foreignkey from customer table
    is_Approved = models.BooleanField(default=False)
    is_Completed = models.BooleanField(default = False)
    is_paid = models.BooleanField(default=False)
    #vehicle_name = vehicles will come here 
    #description = description of problem will come here. 

