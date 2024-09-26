# utils.py
import requests

def get_nasa_apod(api_key, date=None):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
    }
    if date:
        params['date'] = date
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None