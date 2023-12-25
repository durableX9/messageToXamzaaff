from aiogram import types

import kb
from bot import dp, bot
from handlers.fsm import *
from handlers.db import db_profile_exist, db_profile_insertone, db_profile_banned
from configurebot import cfg


welcomemessage = cfg['welcome_message']
errormessage = cfg['error_message']
devid = cfg['dev_id']
question_first_msg = cfg['question_type_ur_question_message']

handler_button_new_question = cfg['button_new_question']


async def client_start(message: types.Message):
    try:
        if(message.chat.type != 'private'):
            await message.answer('This Command Only Used In Private Messaging.')
            return
        if db_profile_exist(message.from_user.id):
            await message.answer(f'{welcomemessage}',parse_mode='Markdown', reply_markup=kb.mainmenu)
        else:
            db_profile_insertone({
                '_id': message.from_user.id,
                'username': message.from_user.username,
                'access': 0,
                'ban': 0
            })
            print('New User!')
            await message.answer(f'{welcomemessage}',parse_mode='Markdown', reply_markup=kb.mainmenu)
    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"*Error* In Chat *{cid}*\nError Status: `{e}`",
                               parse_mode='Markdown')


async def client_newquestion(message: types.Message):
    try:
        if message.text == handler_button_new_question:
            if db_profile_banned(message.from_user.id):
                await message.answer("⚠ You *Blocked* In Bot!", parse_mode='Markdown')
                return
            await message.answer(f"{question_first_msg}")
            await FSMQuestion.text.set()
    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"*Error* In Chat *{cid}*\Error Status: `{e}`",
                               parse_mode='Markdown')


async def client_getgroupid(message: types.Message):
    try:
        await message.answer(f"Chat id is: *{message.chat.id}*\nYour id is: *{message.from_user.id}*", parse_mode='Markdown')
    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"*Error* In Chat *{cid}*\Error Status: `{e}`",
                               parse_mode='Markdown')


def register_handler_client():
    dp.register_message_handler(client_start, commands='start', state=None)
    dp.register_message_handler(client_getgroupid, commands='getchatid')
    dp.register_message_handler(client_newquestion)
