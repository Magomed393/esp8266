from machine import Pin
from time import sleep
import dht

import urequests

sensor = dht.DHT22(Pin(14))
# sensor = dht.DHT11(Pin(14))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        response = urequests.get('http://192.168.43.136:8000/?temp={}&hum={}'.format(temp, hum))
        response.close()
    except OSError as e:
        print('Failed to read sensor.')




