from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
import PostAndSearch.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            PostAndSearch.routing.websocket_urlpatterns
        )
    ),
})


# with websocket security
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': OriginValidator(
#         AuthMiddlewareStack(
#         URLRouter(
#             PostAndSearch.routing.websocket_urlpatterns
#         )
#     ),
#         ['.thewebsite.com', ]
# })