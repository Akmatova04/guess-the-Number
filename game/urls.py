# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.guess_number_view, name='guess_number_url'),
    path('new/', views.new_game_view, name='new_game_url'),
]