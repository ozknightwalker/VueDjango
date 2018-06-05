from __future__ import unicode_literals

from . import viewsets

from Demo.router import router

router.register(r'rooms', viewsets.RoomViewSet)
