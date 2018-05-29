from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        if not email or not password:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return authenticate(email=email, password=password)

    def _validate_username(self, username, password):
        user = None

        if  not username or  not password:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return authenticate(username=username, password=password)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        user = self._validate_username(username, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)
        elif not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)
