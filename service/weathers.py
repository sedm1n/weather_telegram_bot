from aiohttp import ClientSession
import json
import asyncio
import logging
# import openmeteo_requests



logger = logging.getLogger(__name__)

# # response = rq.get('https://api.openweathermap.org/data/2.5/weather?q=Москва,ru&APPID=21b87dc9e79f587e17991a78eb883013')
# data = {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 292.46, 'feels_like': 292.82, 'temp_min': 291.28, 'temp_max': 293.76, 'pressure': 1007, 'humidity': 91, 'sea_level': 1007, 'grnd_level': 988}, 'visibility': 10000, 'wind': {'speed': 2.7, 'deg': 107, 'gust': 7.53}, 'clouds': {'all': 90}, 'dt': 1718652838, 'sys': {'type': 2, 'id': 2094500, 'country': 'RU', 'sunrise': 1718585058, 'sunset': 1718648205}, 'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}
url = 'https://api.openweathermap.org/data/2.5/weather'

# class Weather:
#       def __init__(self, city) -> None:
#             self.city = city
      
#       def _get_weather(self):
#             return rq.get(url).json()
    
#       # @staticmethod
#       # def get_temp()

async def get_coordinates_obdject(city:str):
      
      url_api_search = "https://geocoding-api.open-meteo.com/v1/search?name={}&count=10&language=ru&format=json".format(city)
      async with ClientSession() as session:
            async with session.get(url=url_api_search) as req:
                  response_json:dict = await req.json()
      
      return response_json.get('results') or None

async def request_json(coord:str, current:bool=True, dayli:dict=None) -> dict:

      url = "https://api.open-meteo.com/v1/forecast"
      coordinates = coord.split(":")
      
      params = {
            "latitude": float(coordinates[1]),
            "longitude": float(coordinates[2]),
                 
      }
      
      if current:
            params['current'] = ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "precipitation", "rain", "weather_code", "cloud_cover", "pressure_msl"]

      if dayli:
            params['dayli']= ["temperature_2m_max", "temperature_2m_min","wind_speed_10m_max"],
      
      
      async with ClientSession() as session:
            async with session.get(url=url,params=params) as req:
                  response_json:dict = await req.json()
      
            
      # logger.debug(response_json)
      return response_json

async def get_current_weather(coord:str):
      data = await request_json(coord)
      
      if data.get('current'):
            current:dict = data.get('current')
         
            text = text = f"<b>Температура воздуха:</b> {current.get('temperature_2m')} °C\n"\
                  f"<i>Ощущается как:</i> {current.get('apparent_temperature')} °C\n"\
                  f"<b>Влажность:</b> {current.get('relative_humidity_2m')} %\n"\
                  f"<b>Вероятность дождя:</b> {current.get('rain')} %\n"
                  
      else:
            text:str = "Произошла ошибка, повторите попытку снова"
      
      return text