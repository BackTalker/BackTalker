'''
weather.py
By: Michael Chang
Desc: Check weather at your current location

      Weather output through pyOWN API (Online Weather Network)
      More info: https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples

      Tracking your location is used through IPStack

      Might be useful for location in the future: https://geocoder.readthedocs.io
'''

import json
import requests
from pyowm import OWM
from socket import gethostbyname, gethostname, getfqdn

# Desc: Get current weather
def currentWeather():
    # Get access to the current IP address
    IPAddr = gethostbyname(gethostname())
    # IPAddr = gethostbyname(getfqdn())
    send_url = 'http://api.ipstack.com/{}?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'.format(IPAddr)
    r = requests.get(send_url)  # get ipstack request
    j = json.loads(r.text)      # Load to json form

    print(IPAddr)

    # Create location variable
    city = j['city']                            # City's name  
    region = j['region_code']                   # name of region (Province, State)
    country = j['country_code']                 # name of Country's name
    locateMe = '{},{}'.format(city,country)     # location: city name,Country name

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
    

