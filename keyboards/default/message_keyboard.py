from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from cfgmust import cfg

button_text = cfg['button_new_question']
main_menu_button = KeyboardButton(button_text)

# Creating the main menu markup with the new support button
main_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu_button)
