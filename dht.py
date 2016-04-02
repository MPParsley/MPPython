# Importeer Adafruit DHT bibliotheek.
# -*- coding: utf-8 -*-
import Adafruit_DHT
import datetime

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)

time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
humidity = round(humidity, 2)
temperature = round(temperature, 2)

if humidity is not None and temperature is not None:
  print '{0};{1:0.1f}°C;{2:0.1f}%'.format(time, temperature, humidity)
else:
  print '{0};Failed to read sensor!'.format(time)
