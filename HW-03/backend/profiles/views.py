
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileDetailSer, ProfileUpdateSer, AvatarUpdateSer


class ProfileDetail(generics.RetrieveAPIView):
    """Все Данные о профиле"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    # lookup_field = 'slug'
    serializer_class = ProfileDetailSer

class ProfileUpdate(generics.UpdateAPIView):
    """Редактирование данных пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer

class AvatarProfileUpdate(generics.UpdateAPIView):
    """Редактирование аватара профилья пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSer