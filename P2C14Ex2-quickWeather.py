#! python

import json, requests, os, sys

if len(sys.argv) == 2:
    LOCATION = sys.argv[1]
else:
    print("Please run the program as P2C14Ex2-quickWeather.py [LOCATION]")
    sys.exit()

API_KEY = "" #Enter you API key here

URL = "http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s&cnt=3" % (LOCATION, API_KEY)

print(URL)

response = requests.get(URL)
response.raise_for_status()

jsonData = json.loads(response.text)

weather = jsonData['list']
print('Current weather in %s:' % (LOCATION))
print(weather[0]['weather'][0]['main'], '-', weather[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(weather[1]['weather'][0]['main'], '-', weather[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(weather[2]['weather'][0]['main'], '-', weather[2]['weather'][0]['description'])