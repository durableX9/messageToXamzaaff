from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from cfgmust import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport,)
