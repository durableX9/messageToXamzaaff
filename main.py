from loader import dp
from aiogram.utils import executor

from handlers import client, admin, fsm
from utils.set_bot_commands import set_default_commands
from utils.notifiy_admin import on_startup_notify

async def on_start(dispatcher):
    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


admin.register_handler_admin()
fsm.register_handler_FSM()
client.register_handler_client()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)