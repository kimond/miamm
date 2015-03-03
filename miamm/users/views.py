from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics
from serializers import ProfileSerializer
from users.models import Profile
from users.permissions import IsProfileUser


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileUser,)

    def get_queryset(self):
        """
        This view should return a profile for a user
        """
        user_id = self.kwargs['pk']
        user = User.objects.get(pk=user_id)
        return Profile.objects.filter(user=user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
