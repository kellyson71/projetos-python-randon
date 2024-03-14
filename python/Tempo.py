import requests

def get_weather_forecast(api_key, location):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=1"
    response = requests.get(url)
    data = response.json()

    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"The current temperature in {location} is {temperature}°C with {condition}.")

api_key = 'API_KEY'
location = 'Brazil'  

get_weather_forecast(api_key, location)