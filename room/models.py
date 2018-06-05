from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    session_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='rooms', on_delete=models.PROTECT)
    removed = models.BooleanField(default=False)
    when = models.DateTimeField(auto_now_add=True)
