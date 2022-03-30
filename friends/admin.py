from django.contrib import admin
from .models import FriendList, FriendRequest
# Register your models here.
# admin.site.register(FriendRequest)
# admin.site.register(FriendList)

# trying a different admin set up

class FriendListAdmin(admin.ModelAdmin):
  list_filter = ['user']
  list_display = ['user']
  search_fields = ['user']
  # readonly_fields = ['user']

  class Meta:
    model = FriendList

admin.site.register(FriendList, FriendListAdmin)


class FriendRequestAdmin(admin.ModelAdmin):
  list_filter = ['sender', 'reciever']
  list_display = ['sender', 'reciever']
  search_fields = ['sender__username', 'reciever__email', 'reciever__username', 'reciever__email']

  class Meta:
    model = FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)