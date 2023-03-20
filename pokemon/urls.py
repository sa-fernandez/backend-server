from django.urls import path
from . import views

urlpatterns = [
    
    path('sayHiPokemon/',views.hello_pokemon_world),
    path('getAllPokemons/', views.getAllPokemons),
    path('addPokemon/', views.addPokemon),
    path('getPokemonById/', views.getPokemonById),
    path('getPokemonByName/', views.getPokemonByName),
    path('deletePokemonById/<int:id>', views.deletePokemonById),
    path('updatePokemon/<int:id>', views.updatePokemon),   
    
    
    path('getAllTypes/', views.getAllTypes),
    path('getTypesForPokemon/', views.getTypesForPokemon),
    
    path('getPokemonsFromType/', views.getPokemonsFromType),
    
    path('getAllTypesVsTypes/', views.getAllTypesVsTypes),
    
    path('getPokemonAttachDefenseData/', views.getPokemonAttachDefenseData),
    
    
    
    
]
