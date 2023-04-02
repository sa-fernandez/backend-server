from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

#####----------------------------GET----------------------------#####


@api_view(['GET'])
def getPokemonImage(request):
    print("Getting data")
    baseUrl="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
    try:
        idPokedex = request.GET.get('idPokedex') 
        baseUrl=baseUrl+idPokedex+".png"        
        data={"message": "Success","url":baseUrl}
    except:
        data={"message": "No types found..."}  
    return JsonResponse(data)   


@api_view(['GET'])
def getPokemonShinyImage(request):
    baseUrl="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"
    try:
        idPokedex = request.GET.get('idPokedex') 
        baseUrl=baseUrl+idPokedex+".png"        
        data={"message": "Success","url":baseUrl}
    except:
        data={"message": "No types found..."}  
    return JsonResponse(data)   


@api_view(['GET'])
def getTypeImage(request):
    baseUrl="https://play.pokemonshowdown.com/sprites/types/"
    try:
        typeName = request.GET.get('typeName') 
        baseUrl=baseUrl+typeName+".png"        
        data={"message": "Success","url":baseUrl}
    except:
        data={"message": "No types found..."}  
    return JsonResponse(data)   


#####--------------------------------------------------------#####


