import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_data = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            
            planet_data.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return planet_data

def find_heaviest_planet(planet_data, top_n=3):
    heaviest_planets = []
    
    # Iterate over the number of top planets needed
    for _ in range(top_n):
        if not planet_data:
            break

        # Find the planet with the maximum mass
        max_mass_planet = ''
        max_mass = -1

        for planet in planet_data:
            if planet['mass'] > max_mass:
                max_mass = planet['mass']
                max_mass_planet = planet
        
        # Add the heaviest planet found to the list
        if max_mass_planet:
            heaviest_planets.append(max_mass_planet)
            # Remove the heaviest planet from the list
            planet_data.remove(max_mass_planet)
    return heaviest_planets

planet_data = fetch_planet_data()
heaviest_planets = find_heaviest_planet(planet_data)

for planet in heaviest_planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']}")
