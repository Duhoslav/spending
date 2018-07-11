from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app.check import views
from api import server_api

urlpatterns = [
    url("^check/", views.check),
    url("^api/add_check/", server_api.add_check),
    url("api/get_check/$", server_api.get_check),
]
