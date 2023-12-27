from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport,)
