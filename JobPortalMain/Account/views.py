

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, status
from django.contrib.auth import  get_user_model
from rest_framework.response import Response
from rest_framework.settings import api_settings

User=get_user_model()
from rest_framework.permissions import AllowAny

from .serializers import  UserSerializer,UserRegister,CompanyRegisterSerializer,CompanyLoginSerializer
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


class CompnayLoginView(generics.CreateAPIView):
    queryset = CompanyRegistrationModel.objects.all()
    serializer_class = CompanyLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if email is None:
            return Response({'error': 'Email not informed'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CompanyRegistrationModel.objects.get(email=email)
            # if not user.check_password(request.data['password']):
            #     return Response({'error': 'Email ou senha incorreto'}, status=status.HTTP_400_BAD_REQUEST)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response(
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)




