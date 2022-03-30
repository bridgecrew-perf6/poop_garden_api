from rest_framework import generics
from .serializers import FriendListSerializer, FriendRequestSerializer
from .models import FriendList, FriendRequest
from rest_framework import response, request
from rest_framework import status
# from django.contrib.auth import get_user_model
# Create your views here.

class FriendListList(generics.ListCreateAPIView):

  queryset = FriendList.objects.all()
  serializer_class = FriendListSerializer

class FriendListDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = FriendList.objects.all()
  serializer_class = FriendListSerializer



class FriendRequestList(generics.ListCreateAPIView):

  queryset = FriendRequest.objects.all()
  serializer_class = FriendRequestSerializer

class FriendRequestDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = FriendRequest.objects.all()
  serializer_class = FriendRequestSerializer
