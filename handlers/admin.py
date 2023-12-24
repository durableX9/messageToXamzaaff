from aiogram import types
from bot import dp, bot

from handlers.db import db_profile_access, db_profile_exist, db_profile_exist_user, db_profile_insertone, db_profile_updateone, db_profile_get_username
from keyboards import kb
from config import cfg
from handlers.fsm import *

lvl3name = cfg['3lvl_adm_name']
devid = cfg['dev_id']

def extract_arg(arg):
	return arg.split()[1:]

async def from_admin(message: types.Message):
	try: 
		uid = message.from_user.id

		if(db_profile_access(uid) >= 1):
			args = extract_arg(message.text)
		