from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
      token:str

@dataclass
class OpenWeather:
      appid:str

@dataclass()
class Config:
      bot_token:TgBot
      owm_appid:OpenWeather

def load_config(path:str=None)->Config:

      env = Env()
      env.read_env(path=path)

      return Config(
            bot_token=env('BOT_TOKEN'),
            owm_appid=env('APPID'),)
