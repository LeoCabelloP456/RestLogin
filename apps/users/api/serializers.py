from asyncore import write
from dataclasses import fields
from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style= {'input_type': 'password'}, write_only=True)
 
    class Meta:
        model = User
        fields= ('email', 'username', 'password', 'password2')
        extra_kwargs= {
                    'password': {'write_only': True}
        }
    
    def save(self):
        user = User(
            email= self.validated_data['email'],
            username= self.validated_data['username'],
        ) 
        password= self.validated_data['password'],
        password2= self.validated_data['password2'],

        if password != password2:
            raise serializers.ValidationError({'password': 'Las contraseñas deben coincidir'})
        
        user.set_password(password)
        user.save()
        return user
