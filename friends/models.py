from django.db import models
from django.conf import settings
# Create your models here.

# This is my Model for the entire friend system

class FriendList(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
  friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name='friends')

  
  def __str__(self):
    return f"{self.user.username}'s friends"


  def add_friend(self, friend_to_add):
    '''add a new friend'''
    if self == friend_to_add:
      return 'cannot friend yourself, silly'

    if not friend_to_add in self.friends.all():
      self.friends.add(friend_to_add)
      # self.save() might end up needing

  
  def remove_friend(self, friend_to_remove):
    '''function to remove a friend from friendlist'''
    if self == friend_to_remove:
      return "if you dont love yourself, how in the hell you gonna love somebody else?"

    if friend_to_remove in self.friends.all():
      self.friends.remove(friend_to_remove)


  def unfreind(self, friend_to_remove):
    '''initiate the action of unfriending someone'''
    remover_friends_list = self
    # remove friend from remover friend list
    remover_friends_list.remove_friend(friend_to_remove)
    # remove remover from removed friend's friends list
    friends_list = FriendList.objects.get(user=friend_to_remove)
    friends_list.remove_friend(self.user)


  def is_mutual_friend(self, possible_friend):
    '''is this a friend?'''
    if possible_friend in self.friends.all():
      return True
    return False


class FriendRequest(models.Model):
  '''a friend request consists of 2 main parts- sender, and reciever'''

  sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
  reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciever')
  is_active = models.BooleanField(blank=True, null=False, default=True)
  time_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.sender
    return f"friend request from {self.sender.username} to {self.reciever.username}."


  def accept(self):
    '''accept a friend request. will update both friends's friends lists'''
    reciever_friend_list = FriendList.objects.get(user=self.reciever)

    if reciever_friend_list:
      reciever_friend_list.add_friend(self.sender)
      sender_friend_list = FriendList.objects.get(user=self.sender)

      if sender_friend_list:
        sender_friend_list.add_friend(self.reciever)
        self.is_active = False
        self.save() #might not need this


  def decline(self):
    '''decline a friend request by setting is_ctive field to false'''
    self.is_active = False
    self.save() #might not need this


  def cancel(self):
    '''cancle a friend request by setting is_ctive field to false(same as decline but from the other person)'''
    self.is_active = False
    self.save() #might not need this

  