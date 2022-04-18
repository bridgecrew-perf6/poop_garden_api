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


### I want to either create a new view or edit the view below to only show the poop profiles of a user's friends. This should make things muuuuuuch faster when loading up the front end, becouse i dont have to add poop profiles to every single user for no reason. only my friends. as the app grows this is NECESSARY

# gives us the ability to add items
class PoopProfileList(ListCreateAPIView):

  # permission_classes = (isAuthenticated,)
  serializer_class = PoopProfileSerializer
  # queryset = PoopProfile.objects.all()


  def get_queryset(self):
    user = self.request.user
    friends = Friend.objects.friends(user)
    print(friends)
    queryset = PoopProfile.objects.filter(Q(user__in=friends) | Q(user=user))
    return queryset



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

