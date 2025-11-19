## Load libraries
import requests
import pandas as pd
# import python-dotenv
from dotenv import load_dotenv, set_key
## Set our url and endpoint

BASE_URL = 'https://pokeapi.co/api/v2/'
endpoint = 'pokemon'

## Construct our API path
url_path = f'{BASE_URL}{endpoint}'

response = requests.get(url_path)

## Check status
response.status_code

## Check URL 
print(response.url)

## Extract data.
## .json() converts the response body (a JSON) into a Python Dictionary
data = response.json()

# exercise: print all of the pokemon names for the first page
for pokemon in data['results']:
    print(pokemon.get('name'))

## Iterate over and retrieve each pokemon (pagination)

url_path = f'{BASE_URL}{endpoint}'
pokemon_list = []

# .extend() appends all elements of a list whereas .append() adds a single element 
# to the end of a list

## data.get('results', []) expects a list, and returns an empty list if none is present
## data.get('results') will fail if value returned for key is not a list, and will return None
while url_path:
    response = requests.get(url_path)
    data = response.json()
    pokemon_list.extend(data.get('results',[]))
    url_path = data.get('next')


## Now print all pokemon names, for all pages:
for pokemon in pokemon_list:
    print(pokemon.get('name'))

## Related Resources (primary key)

### Bulbasaur
bulbasaur_data = requests.get(pokemon_list[0].get('url')).json()

## Learn about move
move_url = bulbasaur_data['moves'][0]['move']['url']

move_data = requests.get(move_url).json()


### Open Meteo|| Parameters
BASE_URL = "https://api.open-meteo.com/v1/"
endpoint = 'forecast'
url_path = f'{BASE_URL}{endpoint}'

params = {
	"latitude": 39.3,
	"longitude": -76.61,
	"hourly": ["temperature_2m", "rain"],
	"temperature_unit": "fahrenheit",
}

response = requests.get(url=url_path, params=params)
print(response.url)

data = response.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
rain = data["hourly"]["rain"]

df = pd.DataFrame({
    "Time": pd.to_datetime(times),
    "Temp": temps,
    "Rain": rain
})

### Authentication

BASE_URL = 'https://api.nasa.gov/'
ENDPOINT = 'insight_weather/'

path_url = f'{BASE_URL}{ENDPOINT}'

params = {
    'feedtype': 'json',
    'ver': '1.0',
}

response = requests.get(path_url, params=params)
response.status_code

## Response [403]: Forbidden

API_KEY = 'DEMO_KEY'

params = {
    'feedtype': 'json',
    'ver': '1.0',
    'api_key': API_KEY
}

from dotenv import load_dotenv, set_key
import os
current_directory = os.getcwd()
BASE_URL = 'https://api.nasa.gov/'
ENDPOINT = 'insight_weather/'

API_KEY = os.environ.get('API_KEY')

path_url = f'{BASE_URL}{ENDPOINT}'

params = {
    'feedtype': 'json',
    'ver': '1.0',
    'api_key': API_KEY
}

requests.get(path_url, params=params)