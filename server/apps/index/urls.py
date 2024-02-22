from django.urls import path

from .views import index

urlpatterns = [
    path("", index, kwargs={"rpath": ""}),
    path("<str:rpath>", index),
    path("<str:rpath>/slow", index),
]
