# WatDoIWear -- WIP
Extremely simple webapp that recommends users what they should wear based on their location. 
Built using Python, Flask, the IPStack API and the OpenWeatherMap API. I developed because I wanted this to play around with the OpenWeatherMap API and the IPStack API.

**NOTE:** In order to compile, a config.json file is needed. config.json will hold the api keys needed for OpenWeatherMap and IPStack. The format of config.json must be: 
```
{
    "keys":{
        "openWeatherMap" : "abcd", //replace abcd with openWeatherMap API key
        "ipStack" : "efg"   //replace efg with IPStack API key
    }
}
```

**ADITIONAL NOTE**: I used heroku to deploy this webapp. You can simply clone this repository and deploy this by using the commands below:

```
$ heroku create
$ git push heroku master
$ heroku open
```

See the app in action!: https://shielded-scrubland-82220.herokuapp.com/
