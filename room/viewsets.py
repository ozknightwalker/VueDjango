from __future__ import unicode_literals

from .models import Room
from .serializers import RoomSerializer

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.filter(removed=False)
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
