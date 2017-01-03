#!/usr/bin/env python

import time
from envirophat import light, weather
from beebotte import *

### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT('API_KEY', 'SECRET_KEY')

period = 300 ## Sensor data reporting period (5 minutes)

### Change channel name as suits you - in this instance, it is called Enviro_pHAT
temp_resource   = Resource(bbt, 'Enviro_pHAT', 'temperature')
pressure_resource  = Resource(bbt, 'Enviro_pHAT', 'pressure')
light_resource = Resource(bbt, 'Enviro_pHAT', 'light')

def run():
  while True:
    ### Assume 
    temperature, pressure, lux = weather.temperature() -9, weather.pressure(), light.light()
    if temperature is not None and pressure is not None and lux is not None:
        print ("Temp={0:.1f}*C   Pressure={1:.0f} hPa   Light={2:.0f} lux".format(temperature, pressure, lux))
        try:
          #Send temperature to Beebotte
          temp_resource.write(temperature)
          #Send pressure to Beebotte
          pressure_resource.write(pressure)
          #Send light to Beebotte
          light_resource.write(lux)
        except Exception:
          ## Process exception here
          print ("Error while writing to Beebotte")
    else:
        print ("Failed to get reading. Try again!")

    #Sleep some time
    time.sleep( period )

run()

