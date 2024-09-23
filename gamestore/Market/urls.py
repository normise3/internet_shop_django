from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('all_games/', views.all_games, name='all_games'),
    path('buy_game/<str:game_name>/', views.buy_game, name='buy_game'),
]
