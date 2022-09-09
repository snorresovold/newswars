from django.urls import path

from .views import NewsViewSet, ChannelViewSet

urlpatterns = [
    # path("", NewsViewSet.as_view()),
    path("channel", ChannelViewSet.as_view()),
]