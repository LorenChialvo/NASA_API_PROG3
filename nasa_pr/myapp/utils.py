import requests
from django.conf import settings

def get_nasa_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': 'wPaokkYocPlVLpz9w7HtE1JfLdfcuD0QnH223zTl',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_nasa_api_key():
    return settings.NASA_API_KEY
