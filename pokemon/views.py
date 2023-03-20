from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponse, JsonResponse
from django.views import View
from pokemon.models import Pokemon, PokemonType, PokemonTypeHasType, TypeVsType
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view



# Create your views here.

def hello_pokemon_world(request):
    message = "Hello pokemon!"
    return HttpResponse(message)


#####----------------------------GET----------------------------#####
@api_view(['GET'])
def getAllPokemons(request):
    pokemonQuery = list(Pokemon.objects.values())
    print("Getting all Pokemons...")
    if(len(pokemonQuery)>0):
        data={"message": "Success","data":pokemonQuery}
    else:
        data={"message": "No pokemons found..."}
    return JsonResponse(data)   

@api_view(['GET'])
def getPokemonById(request):
    idPokedex = request.GET.get('idPokedex')
    try:
        pokemon= list(Pokemon.objects.values().filter(idPokedex=idPokedex))[0]
        data={"message": "Success","data":pokemon}
    except:
        data={"message": "No pokemon found..."}  
    return JsonResponse(data)

@api_view(['GET'])
def getPokemonByName(request):
    name = request.GET.get('name')
    try:
        pokemon= list(Pokemon.objects.values().filter(name=name))[0]
        data={"message": "Success","data":pokemon}
    except:
        data={"message": "No pokemon found..."}  
    return JsonResponse(data)


@api_view(['GET'])
def getAllTypes(request):
    types = list(PokemonType.objects.values())
    print("Getting all types...")
    if(len(types)>0):
        data={"message": "Success","data":types}
    else:
        data={"message": "No types found..."}
    return JsonResponse(data)  


@api_view(['GET'])
def getTypesForPokemon(request):
        try:
            idPokedex = request.GET.get('idPokedex')
            pokemon_types_ids = list(PokemonTypeHasType.objects.values().filter(Pokemon_idPokedex=idPokedex))
            pokemon_types_data = [PokemonType.objects.values().get(idType=pt['Type_idType_id']) for pt in pokemon_types_ids]
            data={"message": "Success","data":pokemon_types_data}
        except:
            data={"message": "No types found..."}  
        return JsonResponse(data)  
    
    
@api_view(['GET'])
def getPokemonsFromType(request):
        try:
            idType = request.GET.get('idType')
            pokemon_ids = list(PokemonTypeHasType.objects.values().filter(Type_idType=idType))
            pokemon_data = [Pokemon.objects.values().get(idPokedex=pt['Pokemon_idPokedex_id']) for pt in pokemon_ids]
            data={"message": "Success","data":pokemon_data}
        except:
            data={"message": "No pokemons found..."}  
        return JsonResponse(data)     



@api_view(['GET'])
def getAllTypesVsTypes(request):
    types_vs_types = list(TypeVsType.objects.values())
    data={"message": "Success","data":types_vs_types}
    return JsonResponse(data)    


@api_view(['GET'])
def getAllTypesVsTypes(request):
    types_vs_types = list(TypeVsType.objects.values())
    data={"message": "Success","data":types_vs_types}
    return JsonResponse(data)   


@api_view(['GET'])
def getPokemonAttachDefenseData(request):
    
        try:
            idPokedex = request.GET.get('idPokedex')
            pokemon_types_ids = list(PokemonTypeHasType.objects.values().filter(Pokemon_idPokedex=idPokedex))
            pokemon_attack_data=[]      
            pokemon_defense_data=[]    
                
            for pt in pokemon_types_ids:
                pokemon_attack_data=pokemon_attack_data+list(TypeVsType.objects.values().filter(Attacker=pt['Type_idType_id']))
            
            for pt in pokemon_types_ids:
                pokemon_defense_data=pokemon_defense_data+list(TypeVsType.objects.values().filter(Defender=pt['Type_idType_id']))
                
            data={"message": "Success","attack_data":pokemon_attack_data, "defense_data":pokemon_defense_data}
        except:
            data={"message": "No types found..."}  
        return JsonResponse(data)   
 
#####--------------------------------------------------------#####



#####----------------------------POST----------------------------#####

@csrf_exempt
@api_view(['POST'])
def addPokemon(request):
    if request.method == 'POST':
        new_pokemon = Pokemon.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            generation=request.POST.get('generation'),
            )
        json_response_data= {"message": "Success","details":"Pokemon added","idPokedex":new_pokemon.idPokedex}
        return JsonResponse(json_response_data) 
    else:
        return JsonResponse({'error': 'Invalid request method'})


#####--------------------------------------------------------#####


#####----------------------------DELETE----------------------------#####

@csrf_exempt
@api_view(['DELETE'])
def deletePokemonById(request, id):
    if request.method == 'DELETE':
        pokemon = Pokemon.objects.get(idPokedex=id)
        idPokedex_cp = pokemon.idPokedex
        pokemon.delete()
        return JsonResponse({'message': f'Pokemon with idPokedex= {idPokedex_cp} deleted successfully'})

    else:
        return JsonResponse({'error': 'Invalid request method'})



#####--------------------------------------------------------#####




#####----------------------------PUT----------------------------#####

@csrf_exempt
@api_view(['PUT'])
def updatePokemon(request, id):
    try:
        pokemon = Pokemon.objects.get(idPokedex=id)
    except Pokemon.DoesNotExist:
        return JsonResponse({'message': 'The Pokemon does not exist'}, status=404)

    if request.method == 'PUT':
        pokemon.name = request.POST.get('name', pokemon.name)
        pokemon.description = request.POST.get('description', pokemon.description)
        pokemon.generation = request.POST.get('generation', pokemon.generation)
        pokemon.save()

        return JsonResponse({'message': 'Pokemon updated successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=405)  

#####--------------------------------------------------------#####
