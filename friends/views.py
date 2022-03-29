from rest_framework import generics
from .serializers import FriendListSerializer
from .models import FriendList
from friendship.models import Friend
from rest_framework import response, request
from rest_framework import status
# from django.contrib.auth import get_user_model
# Create your views here.


# gives us the ability to add items
class FriendListList(generics.ListCreateAPIView):
  queryset = FriendList.objects.all()
  serializer_class = FriendListSerializer

# gives us the ability to update and delete
class FriendListDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = FriendList.objects.all()
  serializer_class = FriendListSerializer

# class FriendListList(generics.ListAPIView):

#   queryset = Friend.objects.friends()
#   serializer_class = FriendListSerializer