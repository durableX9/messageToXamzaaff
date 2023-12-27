from environs import Env

env = Env()
env.read_env()

# We Can Read files from .env
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token   
ADMINS = env.list("ADMINS")  # ADMINS
GROUPS = env.list("GROUPS") # Groups
