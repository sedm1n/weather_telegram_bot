from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON
from service.weathers import get_coordinates_obdject
from aiogram.filters.callback_data import CallbackData


class CoordCalbackFacktory(CallbackData, prefix='coord'):
      lat : float
      long : float


async def generate_kb_cities(city:str)-> ReplyKeyboardMarkup:
      keyboard = InlineKeyboardBuilder()
      buttons = []
      cities = await get_coordinates_obdject(city)
      if cities:
            for city in cities:
                  buttons.append(InlineKeyboardButton(text="{}-{}-{}".format(
                        city['name'],
                        city['country'],
                        city['admin1']
                  ), callback_data= CoordCalbackFacktory(
                        lat=city['latitude'],
                        long=city['latitude']
                  ).pack()
                  ))
      
      
      keyboard.row(*buttons, width=1)
      return keyboard.as_markup()


kb_location = ReplyKeyboardMarkup(keyboard=[
                                  [KeyboardButton(text=LEXICON['get_location'], request_location=True)]
                                  ], resize_keyboard=True)
