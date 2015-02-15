from django.shortcuts import render
from rest_framework import generics
from menus.models import Day, Menu, Week
from rest_framework import viewsets
from menus.serializers import MenuSerializer, WeekSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class WeekList(generics.ListCreateAPIView):
    model = Week
    serializer_class = WeekSerializer

    def get_queryset(self):
        """
        This view should return a list of weeks
        """
        menu_id = self.kwargs['pk']
        return Week.objects.filter(menu=menu_id)

    def perform_create(self, serializer):
        menu = Menu.objects.get(pk=self.kwargs['pk'])
        serializer.save(menu=menu)


class WeekDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Week
    serializer_class = WeekSerializer

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
        return obj
