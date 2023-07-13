from django.shortcuts import render
from rest_framework.views import APIView, Response
from accounts.serializers import UserLoginSerializer, UserRegisterSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth import login,authenticate,logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        data=request.data
        serializer=UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    # authentication_classes=(SessionAuthentication,)
    def post(self,request):
        data=request.data
        user=authenticate(username=data['username'],password=data['password'])
        print(user)
        if user:
            login(request,user)
            serializer=UserSerializer(request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        if not user:
            return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    

class UserView(APIView):
    authentication_classes=(SessionAuthentication,)
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserLogoutView(APIView):
    authentication_classes=(SessionAuthentication,)

    def post(self,request):
        logout(request)

        return Response({'message':'User Logged Out'})


