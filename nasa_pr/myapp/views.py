# myapp/views.py
# views.py
import requests
from django.shortcuts import render
from django.conf import settings

def apod_view(request):
    date = request.GET.get('date')
    apod_data = None
    error = None

    try:
        if date:
            url = f'https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}&date={date}'
        else:
            url = f'https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}'
        
        response = requests.get(url)
        response.raise_for_status() 
        apod_data = response.json()
        
        if 'error' in apod_data:
            error = apod_data['error'].get('message', 'An error occurred while fetching data.')
            apod_data = None

    except requests.exceptions.RequestException as e:
        error = f"An error occurred: {str(e)}"

    print("API Response:", apod_data)  # Add this line for debugging
    return render(request, 'apod.html', {'apod_data': apod_data, 'error': error})