from rest_framework import serializers
from .models import FriendList, FriendRequest

class FriendListSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = FriendList

class FriendRequestSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = FriendRequest