from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .serializer import RegistrationSerializer, UserSerializer
from .models import User

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]