from rest_framework import serializers
from .models import FriendList
# from friendship.models import Friend

class FriendListSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = FriendList

# class FriendSerializer(serializers.ModelSerializer):
#   class Meta:
#     fields = '__all__'
#     model = Friend