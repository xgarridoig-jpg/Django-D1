# arquitectura/urls.py
from django.urls import path

from . import views

app_name = "arquitectura"

urlpatterns = [
    path("", views.home, name="home"),
    path("flujo/", views.flujo, name="flujo"),
    path("mvc/", views.mvc, name="mvc"),
]