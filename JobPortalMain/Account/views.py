

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, status
from django.contrib.auth import  get_user_model
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView
User=get_user_model()
from rest_framework.permissions import AllowAny

from .serializers import  UserSerializer,UserRegister,CompanyRegisterSerializer,CompanyTokenObtainPairSerializer
from .models import CompanyRegistrationModel


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegister


class CompanyRegisterView(generics.CreateAPIView):
    queryset = CompanyRegistrationModel.objects.all()
    serializer_class = CompanyRegisterSerializer
    permission_classes = (AllowAny,)


class CompnayLoginView(TokenObtainPairView):

    serializer_class = CompanyTokenObtainPairSerializer
    permission_classes = (AllowAny,)






