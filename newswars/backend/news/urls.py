from django.urls import path

from .views import NewsViewSet

urlpatterns = [
    path("", NewsViewSet.as_view()),
]
