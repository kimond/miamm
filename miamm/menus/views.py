from django.shortcuts import render
from rest_framework import generics
from menus.models import Day, Menu, Week
from rest_framework import viewsets
from menus.serializers import MenuSerializer, WeekSerializer
from menus.permissions import IsOwner, IsMenuOwner
from rest_framework import exceptions
from django.shortcuts import get_object_or_404


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(owner=self.request.user)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsOwner,)


class WeekList(generics.ListCreateAPIView):
    model = Week
    serializer_class = WeekSerializer

    def get_queryset(self):
        """
        This view should return a list of weeks
        """
        menu_id = self.kwargs['pk']
        menu = Menu.objects.get(pk=menu_id)
        if menu.owner != self.request.user:
            raise exceptions.PermissionDenied()
        return Week.objects.filter(menu=menu_id)

    def perform_create(self, serializer):
        menu = Menu.objects.get(pk=self.kwargs['pk'])
        serializer.save(menu=menu)


class WeekDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Week
    serializer_class = WeekSerializer
    permission_classes = (IsMenuOwner,)

    def get_queryset(self):
        """
        This view should return a week in a menu
        """
        menu_id = self.kwargs['pk']
        week_number = self.kwargs['week_number']
        return Week.objects.filter(number=week_number, menu=menu_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
