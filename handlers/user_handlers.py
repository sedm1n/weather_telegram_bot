import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.keyboards import CoordCalbackFacktory, generate_kb_cities, kb_location

from lexicon.lexicon import LEXICON
from service.weathers import get_current_weather


logger = logging.getLogger(__name__)

router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
      await message.answer(LEXICON['/start'], reply_markup=kb_location)


@router.message(Command('weather'))
async def process_weather_command(message:Message):
      await message.answer(LEXICON['/weather'])

@router.message(F.text)
async def answer_weather(message:Message):
      await message.answer('Выберите город из списка', reply_markup= await generate_kb_cities(city=message.text))

      
@router.callback_query(CoordCalbackFacktory.filter())
async def process_get_weather(callback:CallbackQuery, \
                              callback_data:CoordCalbackFacktory):
          
      await callback.message.answer(text=await get_current_weather(callback_data.pack()))
      await callback.answer()

@router.message(F.content_type.in_({'location'}))
async def process_get_weather_in_location(message:Message):
     lat =  message.location.latitude
     long = message.location.longitude

     await message.answer(await get_current_weather("coor:{}:{}".format(lat,long)))
     