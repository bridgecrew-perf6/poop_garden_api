from email.mime import base
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import PoopProfileSerializer, FartProfileSerializer, UserSerializer, CreateUserSerializer
from .models import PoopProfile, FartProfile
from rest_framework import response, request
from rest_framework import status
from .permissions import isOwnerOrReadOnly, AllowAny
from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.


# gives us the ability to add items
class PoopProfileList(ListCreateAPIView):

  # permission_classes = (isAuthenticated,)
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer

# gives us the ability to update and delete
class PoopProfileDetail(RetrieveUpdateDestroyAPIView):
  # permission_classes = (isAuthenticated,)
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer


class FartProfileList(ListCreateAPIView):
  # permission_classes = (isOwnerOrReadOnly,)
  queryset = FartProfile.objects.all()
  serializer_class = FartProfileSerializer

# gives us the ability to update and delete
class FartProfileDetail(RetrieveUpdateDestroyAPIView):
  # permission_classes = (isOwnerOrReadOnly,)
  queryset = FartProfile.objects.all()
  serializer_class = FartProfileSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = CreateUserSerializer

