from rest_framework import generics
from .serializers import PoopProfileSerializer
from .models import PoopProfile
# from friendship.models import Friend
from rest_framework import response, request
from rest_framework import status
# from django.contrib.auth import get_user_model
# Create your views here.


# gives us the ability to add items
class PoopProfileList(generics.ListCreateAPIView):

  def get_queryset(self):

    passed_id = self.request.query_params.get('id')

    if passed_id:
      queryset = PoopProfile.objects.filter(id=passed_id)
    else:
      queryset = PoopProfile.objects.all()
    return queryset

  # queryset = Pooper.objects.filter(email='me@something.com')
  serializer_class = PoopProfileSerializer

# gives us the ability to update and delete
class PoopProfileDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = PoopProfile.objects.all()
  serializer_class = PoopProfileSerializer

# class FriendListList(generics.ListCreateAPIView):

#   queryset = Friend.objects.friends()
#   serializer_class = FriendListSerializer

  


