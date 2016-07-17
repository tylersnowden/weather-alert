import urllib, json
from time import sleep
import config
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
# Setup GPIO Pins for LEDs
GPIO.setup(7, GPIO.OUT)

api = config.weather_api
url = "http://api.openweathermap.org/data/2.5/forecast?id=" + api['city_id'] + "&appid=" + api['app_id']

try:
    response = urllib.urlopen(url)
    weather = json.loads(response.read())

    rain = False
    for j in range(0, 4):
        weather_range = weather['list'][j]['weather']
        for i in range(0, len(weather_range)):
            if weather_range[i]['main'] == 'Rain':
                rain = True

    
    if rain:
        blink_counter = 0
        print 'There will be rain.'

        # Blink for One Hour
        while blink_counter <= 1800:
            # Blink Weather LED
            GPIO.output(7, True)
            # print "Blink On"
            sleep(1)
            GPIO.output(7, False)
            # print "Blink Off"
            sleep(1)
            blink_counter += 1
    else:
        # Wait One Hour
        sleep(3600)

except KeyboardInterrupt:
    GPIO.cleanup()

