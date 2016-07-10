import urllib, json
import config
from datetime import datetime

api = config.weather_api
url = "http://api.openweathermap.org/data/2.5/forecast?id=" + api['city_id'] + "&appid=" + api['app_id']
response = urllib.urlopen(url)
weather = json.loads(response.read())

rain = False
for j in range(0, 4):
    weather_range = weather['list'][j]['weather']
    for i in range(0, len(weather_range)):
        if weather_range[i]['main'] == 'Rain':
            rain = True

if rain:
    print 'There will be rain.'
