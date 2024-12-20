from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/userdata', views.fetch_users_data, name="users"),
]