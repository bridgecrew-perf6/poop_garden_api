from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PoopProfileSerializer, FartProfileSerializer, UserSerializer
from .models import PoopProfile, FartProfile
from rest_framework import response, request
from rest_framework import status
from .permissions import isOwnerOrReadOnly
from django.contrib.auth.models import User

# Create your views here.


# gives us the ability to add items
class PoopProfileList(ListCreateAPIView):

  # permission_classes = (isOwnerOrReadOnly,)
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer

# gives us the ability to update and delete
class PoopProfileDetail(RetrieveUpdateDestroyAPIView):
  # permission_classes = (isOwnerOrReadOnly,)
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


