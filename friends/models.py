from django.db import models
from django.contrib.auth import get_user_model
from friendship.models import Friend


# Create your models here.

class FriendList(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
  friends = models.ManyToManyField(Friend, blank=True, related_name='friends')
  # friends = models.ManyToManyField(get_user_model(), blank=True, related_name='friends')
  

  def __str__(self):
    return self.user