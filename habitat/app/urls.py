# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),    
    path('module1_form', views.module1_form, name='module1_form'),
    path('admin_dashboard', views.getAuthUser, name='auth_user'),
    path('maindashboard', views.maindashboard, name='maindashboard'),
    path('ajax/getdemoInfo', views.getdemoInfo, name='getdemoInfo'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
