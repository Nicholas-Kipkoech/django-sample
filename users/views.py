from django.shortcuts import render
from rest_framework import generics,status
from .serializers import UserSerializer
from .models import User
# Create your views here.

class UserView(generics.CreateAPIView):
    serializer_class=UserSerializer


class UsersList(generics.ListAPIView):
    serializer_class=UserSerializer
    queryset = User.objects.all()

