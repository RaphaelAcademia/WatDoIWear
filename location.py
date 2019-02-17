import json
import requests

class location():
    def __init__(self, APIKey):
        self.key = APIKey

    def getCity(self, ip):    # get city based on ip
        url = 'http://api.ipstack.com/' + str(ip) + '?access_key=' + str(self.key) + '&format=1'
        r = requests.get(url) 
        data = r.json()
        return (data['city'])

    def getLat(self, ip):     # get latitude based on ip
        url = 'http://api.ipstack.com/' + str(ip) + '?access_key=' + str(self.key) + '&format=1'
        r = requests.get(url) 
        data = r.json()
        return (data['latitude'])

    def getLong(self, ip):     # get longitude based on ip
        url = 'http://api.ipstack.com/' + str(ip) + '?access_key=' + str(self.key) + '&format=1'
        r = requests.get(url) 
        data = r.json()
        return (data['longitude'])