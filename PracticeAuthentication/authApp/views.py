from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserModelSerializer ,CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class Register(CreateAPIView):
      serializer_class = UserModelSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer