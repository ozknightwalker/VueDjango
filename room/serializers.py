from __future__ import unicode_literals

from .models import Room

from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('session_id', 'name')
