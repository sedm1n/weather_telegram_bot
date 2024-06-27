import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON

logger = logging.getLogger(__name__)

router = Router()

@router.message()
async def answer_other(message:Message):
      await message.reply(LEXICON['other_answer'])