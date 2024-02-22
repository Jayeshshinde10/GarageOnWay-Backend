from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from api import models
from api import views
router = DefaultRouter()
router.register(prefix='order',viewset=views.OrderViewSet,basename='order')
router.register(prefix='ServiceProvider',viewset=views.ServiceProviderViewSet,basename='ServiceProvider')
router.register(prefix='customer',viewset=views.CustomerViewSet,basename='customer')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path("login/",views.LoginView.as_view()),
    path("register/",views.RegisterView.as_view()),
    path("UsernameExists/",views.CheckUsernameExists.as_view()),
    path('EmailExists/',views.CheckEmailExists.as_view()),
    path('gettoken/',TokenObtainPairView.as_view(),name='access token'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh token'),
    path('getUsername/',views.GetUserName.as_view(),name="get username"),
    path('verifyToken/',TokenVerifyView.as_view(),name='verify token'),
]
