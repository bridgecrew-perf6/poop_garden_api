from rest_framework import serializers
from .models import PoopProfile
from friendship.models import Friend

class PoopProfileSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'user', 'nickname', 'poopInfo', 'created_at', 'updated_at',) # will need to possibly add friends list here as well
    model = PoopProfile

# class FriendListSerializer(serializers.ModelSerializer):
#   class Meta:
#     fields = '__all__'
#     model = Friend