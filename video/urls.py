from __future__ import unicode_literals

from django.urls import path

from .views import HomepageView, LoginView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
]
