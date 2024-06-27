import asyncio
import logging
from re import L
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import load_config, Config
from handlers import other_handlers, user_handlers


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


async def main():
      config:Config = load_config()
      
      bot = Bot(token=config.bot_token, default=DefaultBotProperties( parse_mode=ParseMode.HTML,))
      dp=Dispatcher()
      
      dp.include_router(user_handlers.router)
      # dp.include_router(other_handlers.router)
      
      await dp.start_polling(bot)
      
      logger.info("bot starting ...")
      

if __name__=='__main__':
      asyncio.run(main())







