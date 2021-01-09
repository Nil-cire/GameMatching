# chat/routing.py
from django.urls import re_path, path

from . import consumers


websocket_urlpatterns = [
    path('ws/homepage/game/<english_name>/', consumers.ChatConsumer),
    path('ws/homepage/game/<slug:english_name>/<int:room_id>/', consumers.PrivateChatConsumer),
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]