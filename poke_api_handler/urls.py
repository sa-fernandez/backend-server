from django.urls import path
from . import views

urlpatterns = [    
    path('getPokemonImage/',views.getPokemonImage),
    path('getPokemonShinyImage/',views.getPokemonShinyImage),
    path('getTypeImage/',views.getTypeImage),
]
