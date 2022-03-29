from django.urls import path
from .views import FriendListDetail, FriendListList
urlpatterns = [
  path('<int:pk>/', FriendListDetail.as_view(), name='friend_list_detail'),
  path('', FriendListList.as_view(), name='friend_list_list')
]