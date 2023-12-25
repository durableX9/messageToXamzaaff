# from aiogram import Bot
# from aiogram.dispatcher import Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import configurebot

# storage=MemoryStorage()
# bot = Bot(token=configurebot.cfg['token'])
# dp = Dispatcher(bot, storage=storage)

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)