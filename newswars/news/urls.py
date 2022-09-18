from django.urls import path

from .views import NewsViewSet, ChannelsViewSet

urlpatterns = [
    path("", NewsViewSet.as_view()),
    path("channel", ChannelsViewSet.as_view()),
]