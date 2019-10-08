'''
weather.py
By: Michael Chang
Check weather at your current location

'''

import json
import requests
from pyowm import OWM
from socket import *

def currentWeather():
    IPAddr = gethostbyname(gethostname())
    send_url = 'http://api.ipstack.com/{}?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'.format(IPAddr)
    r = requests.get(send_url)
    j = json.loads(r.text)

    city = j['city']
    region = j['region_code']
    country = j['country_code']

    # print(city)
    # print(region)

    # https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples
    API_keys = '23ae1c41e14442adefb138bcf1efe3c6'
    owm = OWM(API_keys)
    locateMe = '{},{}'.format(city,country)
    obs = owm.weather_at_place(locateMe)
    # print(obs)   
    w = obs.get_weather()

    response = "The weather is now {}°C/{}°F at {}, {} with {}".format(w.get_temperature(unit='celsius')['temp'],
                                                                      w.get_temperature('fahrenheit')['temp'],
                                                                      city, region, w.get_detailed_status())
    # print(response)
    return response
    


