import os
import requests
import json
from datetime import datetime, timedelta

# https://api.openweathermap.org/data/2.5/weather?q=Madison,Wisconsin&units=imperial&appid=API_KEY

class WeatherAPI:
  def __init__(self):
    API_KEY = os.environ["API_KEY"]
    self.API_KEY = API_KEY
    self.url = 'https://api.openweathermap.org/data/2.5/weather?q=Madison,Wisconsin&units=imperial&appid=' + API_KEY
    self.data = None
    self.response = None
    self.date = datetime.now()

  def get_temperature(self):
    if self.data is None and self.date < datetime.now():
      self.response = requests.get(self.url)
      binary = self.response.content
      self.data = json.loads(binary)

    return self.data['main']['temp']






print "Running..."
weather = WeatherAPI()
print weather.get_temperature()