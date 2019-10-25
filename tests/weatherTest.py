# from modules.weather import *
import requests
import json
from socket import *
import os
from urllib.request import urlopen

# gw = os.popen("ip -4 route show default").read().split()
# s = socket(AF_INET, SOCK_DGRAM)
# s.connect((gw[2], 0))

# IPAddr = gethostbyname(gethostname())
# IPAddr = gethostbyname("")
# IPAddr = s.getsockname()[0]
# gateway = gw[2]
# host = gethostname()

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
# IPAddr = data['ip']

# print(IPAddr)
# print("IP: {}, GW: {}, Host: {}".format(IPAddr, gateway, host))

# send_url = 'http://api.ipstack.com/{}?access_key=4e9f9a4d9d5411bd4c9a9f171d6a42ea'.format(IPAddr)
# r = requests.get(send_url)
# j = json.loads(r.text)

city = data['city']
region = data['region']
country = data['country']

print(city)
print(region)
print(country)

# https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html#owm-weather-api-version-2-5-usage-examples
from pyowm import OWM
API_keys = '23ae1c41e14442adefb138bcf1efe3c6'
owm = OWM(API_keys)

locateMe = '{},{}'.format(city,country)

obs = owm.weather_at_place(locateMe)

# print(obs)

w = obs.get_weather()
# print(w.get_temperature(unit='celsius')['temp'])
# print(w.get_temperature('fahrenheit')['temp'])

# print(w.get_detailed_status())

response = "The weather is now {}°C/{}°F at {}, {} with {}".format(w.get_temperature(unit='celsius')['temp'],
                                                                      w.get_temperature('fahrenheit')['temp'],
                                                                      city, region, w.get_detailed_status())

print(response)

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