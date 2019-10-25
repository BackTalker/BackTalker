'''
weather.py
By: Michael Chang
Desc: Check weather at your current location

      Weather output through pyOWN API (Online Weather Network)
      More info: https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples

      Tracking your location is used through ipinfo.io
      More info: https://ipinfo.io

      Might be useful for location in the future: https://geocoder.readthedocs.io
'''

import json
import requests
from socket import *
from pyowm import OWM
from urllib.request import urlopen

# Desc: Get current weather
def currentWeather():

    # Use this link to get access to my current location
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    # Create location variable
    city = data['city']                            # City's name  
    region = data['region']                        # name of region (Province, State)
    country = data['country']                      # name of Country's name
    locateMe = '{},{}'.format(city,country)        # location: city name,Country name

    print(country)
    print(city)
    print(region)

    # Getting the weather report
    API_keys = '23ae1c41e14442adefb138bcf1efe3c6'       # get API keys
    owm = OWM(API_keys)                                 # gett access to OWN
    obs = owm.weather_at_place(locateMe)                # Access to the host local location
    # print(obs)   
    w = obs.get_weather()                   

    # Output the response
    response = "The weather is now {}°C/{}°F at {}, {} with {}".format(w.get_temperature(unit='celsius')['temp'],
                                                                      w.get_temperature('fahrenheit')['temp'],
                                                                      city, region, w.get_detailed_status())
    # print(response)
    return response
    

