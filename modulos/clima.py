import json
import requests
from config import LATITUDE, LONGITUDE

URL = 'https://api.open-meteo.com/v1/forecast'

def climate_search():
    parameters = {
        'latitude' : LATITUDE,
        'longitude' : LONGITUDE,
        'current': 'temperature_2m,wind_speed_10m',
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_probability_max',
        'timezone' : 'auto',
    }
    response = requests.get(URL, params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()

    atual = data['current']
    diaria = data['daily']

    return {
        'temperature' : atual['temperature_2m'],
        'wind' : atual['wind_speed_10m'],
        'max' : diaria['temperature_2m_max'][0],
        'min' : diaria['temperature_2m_min'][0],
        'precepitation' : diaria['precipitation_probability_max'][0],
    }
