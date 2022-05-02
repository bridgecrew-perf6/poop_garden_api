from rest_framework import serializers
from .models import PoopProfile, FartProfile
from django.contrib.auth.models import User
from django.utils.html import escape

class PoopProfileSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'user', 'nickname', 'poopInfo', 'created_at', 'updated_at',) # will need to possibly add friends list here as well
    model = PoopProfile

class FartProfileSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = FartProfile

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
      password = validated_data.pop('password')
      user = super().create(validated_data)
      user.set_password(password)
      user.save()
      return user
    
    def validate_myfield(self, value):
      return escape(value)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
      password = validated_data.pop('password')
      user = super().create(validated_data)
      user.set_password(password)
      user.save()
      return user

    def validate_myfield(self, value):
      return escape(value)