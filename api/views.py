from django.shortcuts import render
from .models import *
from .Serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

def get_username_from_access_token(access_token):
    try:
        # Decode the access token
        decoded_token = AccessToken(access_token)
        
        # Get the user ID from the decoded token
        user_id = decoded_token.payload.get('user_id')
        
        # Retrieve the user object using the user ID
        user = User.objects.get(pk=user_id)
        
        return user.username
    except Exception as e:
        # Handle exceptions (e.g., token validation failure or user not found)
        print(f"Error: {e}")
        return None


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class ServiceProviderViewSet(ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class LoginView(APIView):
    def post(self, request):
        print("the lenght of users is ",User.objects.all().count())
        username = request.data.get('username')
        password = request.data.get('password')
        print("received username is ",username)
        print("received password is ",password)
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            print("user logged in ")
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(APIView):
    def post(self, request):
        status_data = status.HTTP_200_OK
        try:
            username = request.data.get("username")
            fname = request.data.get('fname')
            lname = request.data.get('lname')
            email = request.data.get('email')
            password = request.data.get('password')
            subject = 'Account Created Successfully 😀'
            message = 'Hare Krishna , You have Created account Successfully'
            from_email = 'garageonway@gmail.com'
            recipient_list = [email]
            # html_message = '<p>This is an HTML message.</p>'
            print("reached to sent email")
            # send_mail(subject, message, from_email, recipient_list)
            print("username is ",username)
            print("User does not exist.")
            user =  User.objects.create_user(username, email, password)
            send_mail(subject, message, from_email, recipient_list)
            response = {
                'data':"Account created successfully"
                    }
            status_data=int(status.HTTP_200_OK)

        except Exception as e:
            print("the error is ",e)
            error_name = type(e).__name__  # Get the error name
            print("An error occurred:", error_name)
            response = {
                'data':f"{error_name}"
                    }
            print("an error has occured")
            status_data=int(status.HTTP_401_UNAUTHORIZED)
        finally:
            return Response(response,status=status_data )        

class CheckUsernameExists(APIView):
    def post(self,request):
        response = dict({})
        status_data = int(status.HTTP_200_OK)
        try:
            username = request.data.get("username")
            email = request.data.get("email")
            user_exists = User.objects.filter(username=username).exists()
            if user_exists:
                print("User exists!")
                response = {
                    'data':"username already exist"
                }
                status_data = int(status.HTTP_200_OK)
        except Exception as e:
             print("an error occured")
             response ={
            'data':"an error accured"
            }
             status_data = int(status.HTTP_401_UNAUTHORIZED)
        finally:
            return Response(response,status=status_data)
        
class CheckEmailExists(APIView):
    def post(self,request):
        response = dict({})
        status_data = int(status.HTTP_200_OK)
        try:
            username = request.data.get("username")
            email = request.data.get("email")
            email_exists = User.objects.filter(email=email).exists()
            if email_exists:
                print("email exists!")
                response = {
                    'data':"email already exist"
                }
                status_data = int(status.HTTP_200_OK)
            else :
                response = {
                    'data':"email does not exists"
                }
        except Exception as e:
             print("an error occured")
             response ={
            'data':"an error accured"
            }
             status_data = int(status.HTTP_401_UNAUTHORIZED)
        finally:
            return Response(response,status=status_data)


class ActivateUserView(APIView):
    def get(self,request):
        try:
            username = request.data.get['username']
            user = User.objects.get(username="username")
            user.is_active = True

        except Exception as e:
            print(f'the exception is {e}')
        finally:
            user.save()




class GetUserName(APIView):
     def post(self, request, format=None):
        try:
            access_token = request.data.get('access_token')
            print(f"the token is {access_token}")
            # Decode the access token
            print("the error occurs here")
            print(f"token with replace is {access_token[1:-1]}")
            decoded_token = AccessToken(access_token[1:-1])
            print(decoded_token.payload.get('exp'))
            # Get the user ID from the decoded token
            user_id = decoded_token.payload.get('user_id')
            # Retrieve the user object using the user ID
            user = User.objects.get(pk=user_id)   
            return Response({"username":user.username,'userid':user_id},status=status.HTTP_200_OK)
        except Exception as e:
            # Handle exceptions (e.g., token validation failure or user not found)
            print(f"Error: {e}")
            return Response({"username":'an error occured'},status=status.HTTP_200_OK)
        finally:
            print("Execution Completed")

class CheckEntryExist(APIView):
    def post(self, request):
        status_data = status.HTTP_400_BAD_REQUEST
        try:
            user_id = int(request.data.get('Customer_id'))
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')
            if Customer.objects.filter(Customer_id = user_id).exists():
                print(f'latitude is {latitude} and longitude is {longitude}')
                customer= Customer.objects.get(Customer_id=user_id)
                customer.latitude = latitude
                customer.longitude = longitude
                customer.save()
                status_data= status.HTTP_201_CREATED
            else:
                print("the customer id is ",user_id)
                print("customer does not exists in the table")
                print(f'latitude is {latitude} and longitude is {longitude}')
                customer = Customer(Customer_id=User.objects.get(pk=user_id),latitude=latitude,longitude=longitude)
                customer.save()
                print("data created and saved")
        except Exception as e:
            print("exception is :",e)            
        finally:
            print("finnaly block is called")
        return Response({'message':"data created successfully"},status=status_data)

            

