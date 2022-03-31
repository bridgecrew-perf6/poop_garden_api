from rest_framework import serializers
from .models import PoopProfile, FartProfile

class PoopProfileSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'user', 'nickname', 'poopInfo', 'created_at', 'updated_at',) # will need to possibly add friends list here as well
    model = PoopProfile

class FartProfileSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = FartProfile