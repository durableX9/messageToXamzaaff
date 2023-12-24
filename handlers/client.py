from aiogram import types
from bot import dp, bot
from handlers.fsm import *
from handlers.db import 

from keyboards import kb
from config import cfg


welcome_message = cfg['welcome_message']
devid = cfg['dev_id']
question_to_admin = cfg['question_type_ur_question_message']


handler_button_new_question = cfg['button_question']

async def client_start(message: types.Message):
	try:
		if(message.chat.type != 'private'):
			await message.answer('')
			return
		if db_profile_exist(message.from_user.id):
			await message.answer(f'{welcome_message}', parse_mode='Markdown', reply_markup=kb.mainmenu)
		else:
			dp_profile_insertone({
				'_id': message.from_user.id,
				'username': message.from_user.username,
				'access': 0,
				'ban': 0
				})
				print('New User!')
				await message.answer(f'{welcome_message}', parse_mode='Markdown', reply_markup=kb.mainmenu)

async def client_newquestion(message: types.Message):
	try:
		await message.answer(f"Chat ID Is: *{message.chat.id}*\nYour ID Is: *{message.from_user.id}*", parse_mode='Markdown')

def register_handler_client():
	dp.register_message_handler(client_start, commands='start', state=None)
	dp.register_message_handler(client_getgroupid, commands='getchatid')
	dp.register_message_handler(client_newquestion)