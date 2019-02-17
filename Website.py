## necessary imports
from flask import Flask, render_template, request
import weatherData
import logging
import json
import location
app = Flask(__name__)

## getting api keys from json file
with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    openWeatherMapKey = data['keys']['openWeatherMap']
    ipStackKey = data['keys']['ipStack']

weatherInformation = weatherData.weatherData(openWeatherMapKey)
location = location.location(ipStackKey)    

@app.route("/")
def main():
    ## use these if running on a server

    latitude = location.getLat(request.headers.getlist("X-Forwarded-For")[0])
    longitude = location.getLong(request.headers.getlist("X-Forwarded-For")[0])
    temperature = float(weatherInformation.getTemp(latitude, longitude))
    city = str(weatherInformation.getCity(latitude, longitude))

    ## use these below if running locally

    #latitude = 43.54
    #longitude = -80.24
    #temperature = float(weatherInformation.getTemp(latitude, longitude))
    #city = str(weatherInformation.getCity(latitude, longitude))
    
    if (temperature < 0):
        clothes = 'a jacket'
    elif (temperature > 0 and temperature < 15):
        clothes = 'a sweater'
    elif (temperature > 15):
        clothes = 'shorts'

    weatherInfo = [
        {
            'city': city,
            'temp': str(temperature) + '°C',
            'clothes': clothes
        }
    ]    
    return render_template('weather.html', weatherInfo = weatherInfo)

