from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

storage = MemoryStorage()
bot = Bot(token=config.cfg['token'])
dp = Dispatcher(bot, storage=storage)
