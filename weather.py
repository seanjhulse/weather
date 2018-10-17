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

  def hot(self):
    if self.data is None:
      return False 
    
    temp = self.data['main']['temp']
    return temp >= 80
  
  def warm(self):
    if self.data is None:
      return False 
    
    temp = self.data['main']['temp']
    return temp >= 60 and temp < 80

  def cold(self):
    if self.data is None:
      return False 
    
    temp = self.data['main']['temp']
    return temp >= 40 and temp < 60

  def freezing(self):
    if self.data is None:
      return False 
    
    temp = self.data['main']['temp']
    return temp >= 0 and temp < 40

  def dead(self):
    if self.data is None:
      return False 
    
    temp = self.data['main']['temp']
    return temp < 0 
