
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'Search'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('game/<english_name>/', views.match_room, name='match_room'),
    path('game/<english_name>/<int:room_id>/', views.chat_room, name='chat_room'),
    path('login', LoginView.as_view(template_name='PostAndSearch/login.html'), name='login'),
    # path('search/<int:id>/', views.search, name='search'),
    # path('search/pokemon/SwordShield', views.search, name='search'),
]