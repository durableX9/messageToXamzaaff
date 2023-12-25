from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from configurebot import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport,)
