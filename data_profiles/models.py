from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class PoopProfile(models.Model):
  poopInfo = models.IntegerField()
  nickname = models.CharField(max_length=64)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nickname

class FartProfile(models.Model):
  fartInfo = models.IntegerField()
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username