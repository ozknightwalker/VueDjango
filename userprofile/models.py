from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.get_full_name()
