from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app.main import views
from api import server_api


urlpatterns = [
    url(r"^$", views.home, name="home"),
]
