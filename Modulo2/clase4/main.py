import requests
import json
import webbrowser

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_data_pokemon(pokemon_name):
    api_url = BASE_URL + pokemon_name
    response = requests.get(api_url)

    try:
        pokemon_data = json.loads(response.text)
        sprites = pokemon_data["sprites"]
        pokemon_image = sprites["front_default"]
        webbrowser.open(pokemon_image)

    except Exception as e:
        print('No se encontro al pokemon: ' + e)


if __name__ == '__main__':
    input_pokemon = input('Introduce el nombre del pokemon: ')
    get_data_pokemon(input_pokemon)
