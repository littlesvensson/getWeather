import pyowm
import sys
import os

# Env variables
location = os.environ.get('OWM_CITY', 'Trnava')
try:
  #apiKey = os.environ.get('OWM_API_KEY', '410949e79c084c1ae243676a2614325f')
  apiKey = os.environ('OWM_API_KEY')
except:
    print('OWM_API_KEY not set! The variable needs to be defined to proceed.')
    sys.exit(1)

# Search for current weather in chosen location and get details
owm = pyowm.OWM(apiKey)
mgr = owm.weather_manager()
weather = mgr.weather_at_place(location).weather

# Weather variables
description=weather.detailed_status
temperature=weather.temperature('celsius')['temp']
wind = weather.wind()['speed'] 

print('This is your happy weather reporting!\n\
City: {0},\n\
Weather description: {1},\n\
Temperature: {2} degrees Celsius\n\
Wind Speed: {3} m/sec'.format(location, description, temperature, wind) )

