import requests
import os
from pprint import pprint

def get_current_weather():
    print(" ******* Get Current Weather *******")
    city = input("Enter the city name: ")
    request_url = (f'https://api.openweathermap.org/data/2.5/weather?appid={'API_KEY'}&q={city}&units=imperial')

    weather_data = requests.get(request_url).json()
    # print(weather_data)
    print(f'Current weather for {weather_data['name']}:')
    print(f'Current temperature is {weather_data['main']['temp']:.1f}°')
    print(
      f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')

if __name__ == "__main__":
    get_current_weather()