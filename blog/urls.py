# -*- coding:utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from blog import views


urlpatterns = [

    url('^login/$',views.yewu().login,name='login'),
    url('^register/$',views.yewu().register,name='register'),
    url('^index/$',views.yewu().index),
    url('^cook_login/$',views.yewu().cook_login),
    url('^cook_index/$',views.yewu().cook_index)
]