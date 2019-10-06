'''

ip: "154.20.144.52"
type: "ipv4"
continent_code: "NA"
continent_name: "North America"
country_code: "CA"
country_name: "Canada"
region_code: "BC"
region_name: "British Columbia"
city: "Richmond"
zip: V6V 1A1
latitude: 49.169960021972656
longitude: -123.09098815917969
location: Object {}
time_zone: Object{}
currency: Object{}
connection: Object{}
security: Object{}
'''

import requests
import json

send_url = 'http://api.ipstack.com/154.20.144.52?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'
r = requests.get(send_url)
j = json.loads(r.text)

city = j['city']
region = j['region_code']

print(city)
print(region)

# https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples
from pyowm import OWM
API_keys = '23ae1c41e14442adefb138bcf1efe3c6'
owm = OWM(API_keys)

obs = owm.weather_at_place('Richmon,BC')

print(obs)



'''
import requests
import json

send_url = 'http://api.ipstack.com/154.20.144.52?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'
r = requests.get(send_url)
j = json.loads(r.text)

lat = j['latitude']
lon = j['longitude']

city = j['city']
region = j['region_code']
'''