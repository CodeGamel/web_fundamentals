import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/13/")
json_data = response.text

poke_data = response.json()

print(poke_data["name"].title())
print(poke_data["abilities"][0]["ability"]["name"])
print(poke_data["abilities"][1]["ability"]["name"])



pokemon_names = ["weedle", "bulbasaur", "charmander"]

def main():
    pokemon_names = ["weedle", "bulbasaur", "charmander"]
    for pokemon in pokemon_names:
        data = fetch_pokemon_data(pokemon)
        name = data['name']
        abilities = [ability['ability']['name'] 
        for ability in data['abilities']]
        print(f"Name: {name}")
        print(f"Abilities: {', '.join(abilities)}")
        print()
        average_weight = calculate_average_weight(pokemon_names)

def fetch_pokemon_data(pokemon_names):
    response = requests.get (f"https://pokeapi.co/api/v2/pokemon/{pokemon_names}")
    if response.status_code == 200:
        return response.json()

def calculate_average_weight(pokemon_names):
    response = requests.get (f"https://pokeapi.co/api/v2/pokemon/{pokemon_names}")
    if response.status_code == 200:
        total_weight = 0
        for pokemon in pokemon_names:
            data = fetch_pokemon_data(pokemon_names)
            total_weight += data['weight']
        average_weight = total_weight / len(pokemon_names)
        return average_weight

if __name__ == "__main__":
    main()  
fetch_pokemon_data(pokemon_names)
calculate_average_weight(pokemon_names)
print(pokemon_names)