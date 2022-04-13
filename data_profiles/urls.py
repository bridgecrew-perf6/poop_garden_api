from django.urls import path
from .views import PoopProfileList, PoopProfileDetail, FartProfileList, FartProfileDetail, UserList, UserDetail, UserCreate
urlpatterns = [
  path('poop_profiles/', PoopProfileList.as_view(), name='poop_profile_list'),
  path('poop_profiles/<int:pk>/', PoopProfileDetail.as_view(), name='poop_profile_detail'),
  path('fart_profiles/', PoopProfileList.as_view(), name='poop_profile_list'),
  path('fart_profiles/<int:pk>/', PoopProfileDetail.as_view(), name='poop_profile_detail'),
  path('users/', UserList.as_view()),
  path('users/<int:pk>/', UserDetail.as_view()),
  path('create_user/', UserCreate.as_view()),
]