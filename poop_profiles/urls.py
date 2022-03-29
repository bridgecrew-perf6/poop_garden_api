from django.urls import path
from .views import PoopProfileList, PoopProfileDetail
urlpatterns = [
  path('', PoopProfileList.as_view(), name='poop_profile_list'),
  path('<int:pk>/', PoopProfileDetail.as_view(), name='poop_profile_detail'),
  # path('<int:pk>/friends', FriendListList.as_view(), name='friend_list')
]