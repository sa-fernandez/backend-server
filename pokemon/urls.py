from django.urls import path
from . import views

urlpatterns = [
    
    path('sayHiPokemon/',views.hello_pokemon_world),
    path('getAllPokemons/', views.getAllPokemons),
    path('getPokemonById/', views.getPokemonById),
    path('addPokemon/', views.addPokemon),
    path('getPokemonByName/', views.getPokemonByName),
    path('deletePokemonById/<int:id>', views.deletePokemonById),
    path('updatePokemon/<int:id>', views.updatePokemon),   
    
    
    path('getAllTypes/', views.getAllTypes),
    path('getTypeById/', views.getTypeById),
    path('getTypesForPokemon/', views.getTypesForPokemon),
    
    path('getPokemonsFromType/', views.getPokemonsFromType),
    path('getPokemonsFromWord/', views.getPokemonsFromWord),
    
    path('getAllTypesVsTypes/', views.getAllTypesVsTypes),
    
    path('getPokemonAttachDefenseData/', views.getPokemonAttachDefenseData),
    
    
    
    
]
