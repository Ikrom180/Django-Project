from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"), #id means only number receive
    path("", views.home, name="home")
]