# Backend 💥
REST API made with Django.


## Runnning

First you need to build the dockerfile, it can be achieve with the following command:

```sh
docker build -t mypokemon .
```


Then, you can run the image to execute the container, it can be achieve with the following command:

```sh
docker run -p 8000:8000 mypokemon
```

👽 Feel free to make any changes in the code 👽


### Endpoints

For the Pokemon project there were defined the necessary endpoints for the CRUD, this one's will be described below:

| Request Type | Endpoints |Description|Params|Body|
| ------ | ------ | ------ | ------ | ------ |
| GET | http://127.0.0.1:8000/api/sayHiPokemon/ |This endpoint has the unique purpose to test the conection with the server, if it works it will return the message "Hello pokemon!"|
| GET | http://127.0.0.1:8000/api/getAllPokemons/ |This endpoint has the purpose to return all the pokemons available |
| GET | http://127.0.0.1:8000/api/getPokemonById/ |This endpoint has the purpose to return a pokemon base on the id.|idPokedex ej. idPokedex=1|
| GET | http://127.0.0.1:8000/api/getPokemonByName/ |This endpoint has the purpose to return a pokemon base on the name.|name ej. name=Pikachu|
| GET | http://127.0.0.1:8000/api/getAllTypes/ |This endpoint has the purpose to return all the types.||
| GET | http://127.0.0.1:8000/api/getTypeById/ |This endpoint has the purpose to return a type base on the id.|idType ej. idType=1|
| GET | http://127.0.0.1:8000/api/getTypesForPokemon/ |This endpoint has the purpose to return all the types of a pokemon.|idPokedex ej. idPokedex=1|
| GET | http://127.0.0.1:8000/api/getPokemonsFromWord/ |This endpoint has the purpose to return all the pokemons associated to an specific word that exists in their names|word ej. word=ar|
| GET | http://127.0.0.1:8000/api/getPokemonsFromType/ |This endpoint has the purpose to return all the pokemons associated to an specific type|idType ej. idType=1|
| GET | http://127.0.0.1:8000/api/getAllTypesVsTypes|This endpoint has the purpose to return all Types VS Types (Attacker vs Defender) data|
| GET | http://127.0.0.1:8000/api/getPokemonAttachDefenseData/ |This endpoint has the purpose to return all the attack and defense data associated to an specific pokemon base on its id|idPokedex ej. idPokedex=1|
| DELETE | http://127.0.0.1:8000/api/deletePokemonById/{ID} |This endpoint has the purpose to delete a pokemon base on the id. the {ID} should be replace with the id of the pokemon to be deleted. ej 20 , 1 , 4.|
| POST | http://127.0.0.1:8000/api/addPokemon/ |This endpoint has the purpose to add a pokemon base on the form-data on the body||name, description, generation. __ej: name=Pokemon prueba 10, description= Descripción prueba 10,generation=1 |
| PUT | http://127.0.0.1:8000/api/updatePokemon/{ID} |This endpoint has the purpose to update a pokemon base on the form-data on the body and the id of the pokemon. the {ID} should be replace with the id of the pokemon to be updated. ||name, description, generation. __ej: name=Pokemon prueba 10, description= Descripción prueba 10,generation=1 |
