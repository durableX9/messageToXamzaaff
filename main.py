from loader import dp
from aiogram import executor

from handlers.admins import admin_handler
from handlers.users import client_handler
from states import newquestion
from utils.set_bot_commands import set_default_commands
from utils.notifiy_admin import on_startup_notify

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


admin_handler.register_handler_admin()
newquestion.register_handler_FSM()
client_handler.register_handler_client()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
