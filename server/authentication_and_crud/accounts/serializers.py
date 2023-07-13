from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

    def create(self,data):
        user_obj=User.objects.create_user(username=data['username'],password=data['password'],email=data["email"])
        return user_obj
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

    def create(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not User:
            raise ValueError("User Not Found")

        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"