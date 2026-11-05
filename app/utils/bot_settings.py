from aiogram import Bot

<<<<<<<< HEAD:app/utils/bot_settings.py
from app.utils.settings import settings
========
from utils.settings import settings
>>>>>>>> 0f966f47802b493d2dbda33278c2d55f97aa14c0:utils/bot_settings.py

bot = Bot(token=settings.BOT_TOKEN)