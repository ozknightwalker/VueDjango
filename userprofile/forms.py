from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    password2 = forms.Charfield(max_legth=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
