import json
import requests

class weatherData():
    def __init__(self, APIkey):
        self.key = APIkey

    def getTemp(self, lat, lon):    # getting the temperature based on the latitude and longitude
        location = {'lat': str(lat), 'lon': str(lon),'appid': str(self.key), 'units': 'metric'}
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?', params = location) # get weather data
        weatherData = r.json()
        return (weatherData['main']['temp'])

    def getCity(self, lat, lon):    # getting the city based on the location
        location = {'lat': str(lat), 'lon': str(lon),'appid': str(self.key), 'units': 'metric'}
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?', params = location) # get weather data
        weatherData = r.json()
        return (weatherData['name'])
        