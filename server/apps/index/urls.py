from django.urls import path

from .views import index, slow

urlpatterns = [
    path("", index, kwargs={"rpath": ""}),
    path("<str:rpath>", index),
    path("slow/<str:rpath>", slow),
]
