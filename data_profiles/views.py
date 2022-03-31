from rest_framework import generics
from .serializers import PoopProfileSerializer, FartProfileSerializer
from .models import PoopProfile, FartProfile
from rest_framework import response, request
from rest_framework import status
from .permissions import isOwnerOrReadOnly
# Create your views here.


# gives us the ability to add items
class PoopProfileList(generics.ListCreateAPIView):

  permission_classes = (isOwnerOrReadOnly,)
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer

# gives us the ability to update and delete
class PoopProfileDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer


class FartProfileList(generics.ListCreateAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = FartProfile.objects.all()
  serializer_class = FartProfileSerializer

# gives us the ability to update and delete
class FartProfileDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (isOwnerOrReadOnly,)
  queryset = FartProfile.objects.all()
  serializer_class = FartProfileSerializer

  


