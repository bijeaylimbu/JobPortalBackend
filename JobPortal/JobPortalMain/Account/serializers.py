from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import  get_user_model
from django.core.validators import validate_email
User=get_user_model()
from .models import  CompanyRegistrationModel
from rest_framework.validators import  UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')


    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserRegister(serializers.ModelSerializer):
    email=serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(write_only=True, required=True)
    password2=serializers.CharField(write_only=True, required=True)

    class Meta:
        model=User
        fields=('username','email','password','password2','first_name','last_name')

    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({'password':"password doesn't match"})

        return attrs

    def create(self, validated_data):
        user=User.objects.create(

            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return  user

    def validate_email(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise  serializers.ValidationError('email is invalid')
        return email



class CompanyRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyRegistrationModel
        fields=('company_name','email','contact_number','password','password1','place')


# class CompanyTokenObtainPairSerializer(TokenObtainPairSerializer):
#    @classmethod
#    def get_token(cls,user):
#        token=super(CompanyTokenObtainPairSerializer,cls).get_token(user)
#
#        token['username']=user.username
#        return token









