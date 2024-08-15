# API key from https://home.openweathermap.org
# Example: https://api.openweathermap.org/data/2.5/weather?q=helsingborg,SE&appid=1cfeaa1311333f786b8a9780aa80c572

import requests
import discord

OWM_EP = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "1cfeaa1311333f786b8a9780aa80c572"
WEATHER_PARAMETERS = {
    "lat": 56.198941,
    "lon": 12.562008,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}

def five_day_forecast():
    r = requests.get(OWM_EP, params=WEATHER_PARAMETERS)
    return r.json()

data = five_day_forecast()
 # Check if there will be rainy weather in the next 12h


for entry in data['list']:
    if entry['weather'][0]['id'] < 700:
        print("Bring an umbrella!")
        break