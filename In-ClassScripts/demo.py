import requests
from dotenv import load_dotenv
import os
#API_KEY = 'zaCELgL0imfnc8mVLWwsAawjYr4RxAf50DDqtl'
API_KEY = 'DEMO_KEY'
BASE_URL = 'https://api.nasa.gov/'
ENDPOINT = 'insight_weather/'

path_url = f'{BASE_URL}{ENDPOINT}'

params = {
    'feedtype': 'json',
    'ver': '1.0',
    'api_key': API_KEY
}

response = requests.get(path_url, params=params)

print(response.url)
os.environ.get('API_KEY')