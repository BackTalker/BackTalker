# from modules.weather import *
import requests
import json

send_url = 'http://api.ipstack.com/154.20.144.52?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'
r = requests.get(send_url)
j = json.loads(r.text)

city = j['city']
region = j['region_code']
country = j['country_code']

print(city)
print(region)
print(country)

# https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples
from pyowm import OWM
API_keys = '23ae1c41e14442adefb138bcf1efe3c6'
owm = OWM(API_keys)

obs = owm.weather_at_place('Vancouver,CA')

# print(obs)

w = obs.get_weather()
# print(w.get_temperature(unit='celsius')['temp'])
# print(w.get_temperature('fahrenheit')['temp'])

# print(w.get_detailed_status())

response = "The weather is now {}°C/{}°F at {}, {} with {}".format(w.get_temperature(unit='celsius')['temp'],
                                                                      w.get_temperature('fahrenheit')['temp'],
                                                                      city, country, w.get_detailed_status())

print(response)