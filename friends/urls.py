from django.urls import path
from .views import FriendListList, FriendListDetail, FriendRequestList, FriendRequestDetail
urlpatterns = [
  path('', FriendListList.as_view(), name='friend_list_list'),
  path('<int:pk>/', FriendListDetail.as_view(), name='friend_list_detail'),

  path('requests/', FriendRequestList.as_view(), name='friend_list_list'),
  path('requests/<int:pk>/', FriendRequestDetail.as_view(), name='friend_list_detail'),
]