import sys
import logging
from typing import Dict

import telegram.error
from telegram import Bot, Update, BotCommand
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler,
)

from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
    KeyboardButtonPollType, InlineKeyboardButton, InlineKeyboardMarkup
)

from bot.handlers.menu.menu import command_menu
from bot.handlers.schedule.cities import command_select_city, command_select_region_city
from bot.handlers.schedule.schedule import command_schedule
from bot.handlers.start.start import command_start

from bot.models import User
from oraza_bot.celery import app
from oraza_bot.settings import TELEGRAM_TOKEN, DEBUG

from telegram import Update
from telegram.ext import CallbackContext
from bot_messages.models.message import Message


def cmd_stop(update: Update, context: CallbackContext):
    text = """Пока в разработке"""
    update.callback_query.message.reply_text(text)


def setup_dispatcher(callback):
    # start
    callback.add_handler(CommandHandler("start", command_start))

    # change language
    callback.add_handler(CallbackQueryHandler(command_menu, pattern='kz'))
    for i in range(10):
        if(i == 0):
            callback.add_handler(CallbackQueryHandler(
                command_select_city, pattern=f'cmd_{i}'))
        callback.add_handler(CallbackQueryHandler(
            cmd_stop, pattern=f'cmd_{i}'))

    callback.add_handler(CallbackQueryHandler(
        command_select_region_city, pattern='select_region_city'))

    callback.add_handler(CallbackQueryHandler(
        command_schedule, pattern=f'city_'))

    callback.add_handler(CallbackQueryHandler(cmd_stop, pattern='ru'))

    return callback


def run_pooling():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"'{bot_link}' started")
    updater.start_polling()
    updater.idle()


bot = Bot(TELEGRAM_TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")
    sys.exit(1)
