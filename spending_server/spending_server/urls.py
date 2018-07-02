from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app import main, check
from api import server_api


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('app.main.urls')),
    url(r'^', include('app.check.urls')),
]
