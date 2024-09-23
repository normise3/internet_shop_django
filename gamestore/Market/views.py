from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    games = Game.objects.order_by('?')[:6]
    return render(request, 'home.html', {'games': games})


def about_us(request):
    return render(request, 'about_us.html')


def all_games(request):
    games = Game.objects.all()
    return render(request, 'all_games.html', {'games': games})


def buy_game(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    return render(request, 'buy_game.html', {'game': game})
