import json
import requests
lat = '28.422662d'
long = '77.037602'
radius = '30'
cities_url = f"http://api.geonames.org/findNearbyPlaceNameJSON?lat={lat}&lng={long}&radius={radius}&username=deepak"
cities_json = requests.get(cities_url).json()['geonames']
for city in cities_json:
    print(city['name'])
