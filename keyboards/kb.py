from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import cfg

mainmenu_question = KeyboardButton(cfg['button_question'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenu_question)
