from __future__ import unicode_literals

from django.contrib.auth import login, logout

from .serializers import LoginSerializer

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def process_login(self):
        login(self.request, self.user)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.process_login()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     data = request.data
    #
    #     username = data.get('username', None)
    #     password = data.get('password', None)
    #
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #
    #             return Response(status=status.HTTP_200_OK)
    #         else:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
