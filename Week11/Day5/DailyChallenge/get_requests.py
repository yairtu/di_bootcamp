import requests
import json


# response['results']['name'] is the name of the pokemon
# response['results']['url'] is the url of the pokemon
def get_all_pokemon_names():
	response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000&offset=1').json()['results']
	return response


def get_pokemon_by_id(name):
	pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
	return pokemon.json()


def all_pokemon_types():
	pokemon_types = requests.get('https://pokeapi.co/api/v2/type').json()['results']
	return pokemon_types


def all_pokemon_by_type(pokemon_type):
	all_by_type = requests.get(f"https://pokeapi.co/api/v2/type/{pokemon_type}").json()['pokemon']
	return all_by_type

