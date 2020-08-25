#! usr/bin/python
# -*- coding:utf-8 -*-
# @Author: winston he
# @File: routing.py
# @Time: 2020-08-25 14:11
# @Email: winston.wz.he@gmail.com
# @Desc:
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import room.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    ),
})


