# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home-screen', views.homescreen, name="homescreen"),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
