#! usr/bin/python
# -*- coding:utf-8 -*-
# @Author: winston he
# @File: urls.py
# @Time: 2020-08-25 14:05
# @Email: winston.wz.he@gmail.com
# @Desc:
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^room/(?P<room_name>\w+)/$', views.ChatRoomView.as_view(), name='room'),
]
