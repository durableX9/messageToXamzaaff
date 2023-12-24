from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import dp, bot

from config import cfg

sup_chat_id = cfg['sup_chat_id']
message_sended = cfg['question_ur_sended_message']


class FSMQuestion(StatesGroup):
	text = State()


# Proccessing
async def newquestion(message: types.Messagem state: FSMContext):
	async with state.proxy() as data:
		if (message.content_type == 'photo'):
			data['text'] = message.caption
		else:
			data['text'] = message.text

		await state.finish()
		
		if(message.chat.username == None):
			who = 'Username Not Exists'
		else:
			who = "@"+message.chat.username
		question = data['text']
		if(message.content_type=='photo'):
			ph = message.photo[0].file_id
			await message.reply(f"{message_sended}",
													parse_mode='Markdown')
			await bot.send_photo(sup_chat_id, ph, caption=f"📨 | New Question\nFrom: {who}\nQuestion: '{data['text']}'\n\nTo Answer For This Question Type"
																													"/answer {message.chat.id} Your Answer", 
																													parse_mode='Markdown')
		else:
			await message.reply(f"{message_sended}",
													parse_mode='Markdown')
			await bot.send_message(sup_chat_id, f"📨 | New Question\nFrom: {who}\nQuestion: '{data['text']}'\n\nTo Answer For This Question Type"
																													"/answer {message.chat.id} Your Answer", 
																													parse_mode='Markdown')

def register_handler_FSM():
	dp.register_message_handler(newquestion, state=FSMQuestion.text, content_types=['photo', 'text'])