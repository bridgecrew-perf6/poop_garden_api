from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import PoopProfileSerializer, FartProfileSerializer, UserSerializer, CreateUserSerializer
from .models import PoopProfile, FartProfile
from rest_framework import response, request
from rest_framework import status
from friendship.models import Friend
from .permissions import isOwnerOrReadOnly, AllowAny
from rest_framework import permissions
from django.contrib.auth.models import User
from django.db.models import Q
# from django.contrib.auth import get_user_model

from django.conf import settings

# Create your views here.


class PoopProfileList(ListCreateAPIView):

  serializer_class = PoopProfileSerializer

  def get_queryset(self):
    user = self.request.user
    friends = Friend.objects.friends(user)
    print(friends)
    queryset = PoopProfile.objects.filter(Q(user__in=friends) | Q(user=user))
    return queryset


class PoopProfileDetail(RetrieveUpdateDestroyAPIView):
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer


class FartProfileList(ListCreateAPIView):
  queryset = FartProfile.objects.all()
  serializer_class = FartProfileSerializer

class FartProfileDetail(RetrieveUpdateDestroyAPIView):
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

